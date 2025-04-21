from typing import List, Dict
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import warnings

warnings.filterwarnings("ignore")
class Analyzer:
    """
    Single responsibility: extract structured insights via LLM with strong prompt engineering.
    """
    def __init__(self, llm: ChatOllama):
        self.llm = llm

        # A shared system‑style preamble to remind the LLM of its role
        self.system_preamble = (
            "You are a highly experienced market research analyst. "
            "You produce concise, accurate industry intelligence based ONLY on the provided context. "
            "If something isn’t supported by the context, reply “Not enough information.”"
        )

    def _run(self, template: str, **kwargs) -> str:
        prompt = self.system_preamble + "\n\n" + template
        chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate.from_template(prompt)
        )
        # invoke (mfrod a3ml switch)
        return chain.run(**kwargs).strip()

    def analyze(self, sources: List[Dict], query: str) -> Dict:
        # Create a single block of context
        context = "\n".join(src["text"] for src in sources)[:12000]

        # 1 Identify top 5 competitors
        comp_tpl = (
            "User Query: \"{query}\"\n\n"
            "Context (delimited by triple backticks):\n"
            "```{context}```\n\n"
            "Task: List the top FIVE companies competing in this market, one per line, in order of market leadership"
            "Do NOT include any additional text or commentary."
        )
        raw_companies = self._run(comp_tpl, query=query, context=context)
        companies = [line.strip() for line in raw_companies.split("\n") if line.strip()][:5]

        # 2 Generate a one‑sentence strategic note for each
        competitors = []
        for company in companies:
            note_tpl = (
                "User Query: \"{query}\"\n"
                "Company: {company}\n\n"
                "Context:\n```{context}```\n\n"
                "Task: In one sentence, summarize this company’s current strategic position "
            )
            note = self._run(note_tpl, query=query, company=company, context=context)
            competitors.append({"name": company, "note": note})

        # 3 Extract (N) key market trends --> '' should have used pydantic ''
        trends_tpl = (
            "User Query: \"{query}\"\n\n"
            "Context:\n```{context}```\n\n"
            "Task: Extract FIVE distinct bullet‑point trends given the user query based on the context and your knowledge"
            "Return each trend on its own line prefixed by a dash ('- ')"
        )
        raw_trends = self._run(trends_tpl, query=query, context=context)
        trends = [t.lstrip("-  ").strip() for t in raw_trends.split("\n") if t.strip().startswith("-")][:5]

        # 4 Produce three strategic recommendations
        recs_tpl = (
            "User Query: \"{query}\"\n\n"
            "Context:\n```{context}```\n\n"
            "Task: Provide THREE numbered, actionable strategic recommendations to dive in this market "
            "Use the format '1. Recommendation text'"
        )
        raw_recs = self._run(recs_tpl, query=query, context=context)
        recommendations = [r.lstrip("1234. ").strip() 
                           for r in raw_recs.split("\n") if r.strip() and r.strip()[0].isdigit()][:3]

        return {
            "competitors": competitors,
            "trends": trends,
            "recommendations": recommendations
        }

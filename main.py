import sys, os
from dotenv import load_dotenv
from research import Researcher
from analysis import Analyzer
from report import ReportWriter
from langchain_ollama import ChatOllama

def main():
    load_dotenv()

    # 1) Read the query
    query = sys.argv[1] if len(sys.argv) > 1 else \
        "Generate a strategy intelligence report for the electric vehicle market and its key players"

    # 2) Instantiate services
    max_s = int(os.getenv("MAX_SOURCES", 10))
    researcher = Researcher(max_sources=max_s)

    llm = ChatOllama(
        model=os.getenv("OLLAMA_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        temperature=float(os.getenv("LLM_TEMPERATURE", 0.0)),
        max_tokens=int(os.getenv("LLM_MAX_TOKENS", 8192)),
    )
    analyzer = Analyzer(llm=llm)

    output_dir = os.getenv("OUTPUT_DIR", "output")
    writer = ReportWriter(output_dir=output_dir)

    # 3) Orchestrate the three stages
    sources = researcher.fetch(query)
    insights = analyzer.analyze(sources, query)
    writer.write(query, insights, sources)

if __name__ == "__main__":
    main()
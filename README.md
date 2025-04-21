# Autonomous Intelligence Report Generator

Turn any high‑level business query into a polished, board‑ready DOCX report—completely offline—using your local Llama‑3 model via Ollama.

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation & Setup](#installation--setup)  
4. [Configuration](#configuration)  
5. [Usage](#usage)  
   - [CLI Mode](#cli-mode)  
6. [Project Structure](#project-structure)  
7. [Architecture](#architecture)  
8. [Next Steps & Extensions](#next-steps--extensions)  
9. [Contributing](#contributing)  
10. [License](#license)  

---

## Features

- **One‑command pipeline** from query to `.docx` report  
- **Web research** via DuckDuckGo + mini‑scraper  
- **Insight extraction**:  
  - Top 5 competitors & one‑sentence notes  
  - Five market trends  
  - Three actionable recommendations  
- **Professional report writer** using `python‑docx`  
- **Fully modular**—swap search, analysis or report modules easily  
- **Offline inference** with a local Llama‑3 model (no cloud API calls)  

---

## Requirements

- Python 3.9+  
- Ollama CLI & local model (e.g. `llama3`)  
- Git  

---
## Architecture

User/CLI or API\
       ↓\
  main.py / api.py\
       ↓\
[1] Research Module\
       ↓\
[2] Analysis Module --> LLM  
       ↓\
[3] Report Module\
       ↓\
     output/


## Installation & Setup

1. **Clone the repository**  
   git clone https://github.com/Ghunemi/autonomous-intelligence-report-generator.git \
   cd autonomous-intelligence-report-generator

   
2. **Create & activate a virtual environment**
python3 -m venv venv\
source venv/bin/activate


3. **Install Python dependencies**
pip install -r requirements.txt\
Copy & edit environment variables 


4. **Configure environment**
cp .env.example .env 

5. **Pull & serve your local model**
ollama pull llama3\
ollama serve & 


## Configuration
##### Edit your .env to customize:

OLLAMA_MODEL=llama3\
OLLAMA_BASE_URL=http://localhost:11434 \
MAX_SOURCES=10 \
LLM_TEMPERATURE=0.0\
LLM_MAX_TOKENS=2048\
OUTPUT_DIR=output


## Usage
##### Run the full pipeline with:
  python main.py "Generate a strategy intelligence report for the electric vehicle market and its key players"\
Your report will be saved in the output/ directory as a Word document.

## Project Structure

├── main.py                 # CLI entry point\
├── research.py             # DuckDuckGo search & scraper\
├── analysis.py             # LLM‑powered insight extraction\
├── report.py               # DOCX report writer\
├── pipeline.py             # (optional) combined sequential pipeline\
├── requirements.txt
├── .env.example\
└── docs/\
    └── architecture.txt    # ASCII architecture diagram\



## Next Steps & Extensions
•Vector‑store memory (Chroma/Qdrant) for RAG & follow‑up Q&A\
•Multi‑agent orchestration (AutoGen/CrewAI) for parallel pipelines\
•Scheduled reports (GitHub Actions, Prefect)\
•Dashboard & API (FastAPI + Streamlit)\
•Model flexibility (GPT‑4, Claude, Llama‑cpp)\

## Contributing
Contributions welcome!\
Open issues or submit PRs to:\
•Swap search provider (SerpAPI, Statista)\
•Integrate a vector database\
•Add new output formats (PDF, HTML)\
•Improve prompts & error handling\

## License
This project is licensed under the MIT License.

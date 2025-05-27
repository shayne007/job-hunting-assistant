# Job hunting assistant
This is a AI assitant project implemented by python using LLM and relative technics, which aims to help me to find a job.

## Features
- Web crawcle to collect the job descriptions published on the internet.
- According to the market investigation and requirements, optimizing the resume to match the most needed position

## Key Tech Highlight
- LLM's superpower to optimizing text structure
- RAG statege to supply rich context for LLM
- MCP Server to provide the tools LLM need when to take actions

## System Architecture

```mermaid
graph TB
    subgraph "Entry Point"
        A[__init__.py] --> B[server.py]
    end
    
    subgraph "Core Server"
        B --> C[JobSearchMCPServer]
        C --> D[FastMCP Instance]
        C --> E[Logger Configuration]
    end
    
    subgraph "Tools Layer"
        F[JobTools Class] --> G[get_joblist_by_expect_job]
        F --> H[get_job_by_resume]
        C --> F
    end
    
    subgraph "LLM Integration"
        I[LLMClient] --> J[OpenAI Client]
        J --> K[DeepSeek API]
        F -.-> I
    end
    
    subgraph "Web Scraping"
        L[listjob.py] --> M[Selenium WebDriver]
        M --> N[BOSS直聘网站]
        G --> L
    end
    
    subgraph "Prompt Management"
        O[prompt.py] --> P[Job_Search_Prompt Template]
        H --> O
    end
    
    subgraph "External Dependencies"
        N[BOSS直聘网站]
        K[DeepSeek API]
        Q[Local job.txt file]
        G --> Q
    end
    
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style F fill:#e8f5e8
    style I fill:#fff3e0
    style L fill:#fce4ec
```
## Data Flow

- Client requests job recommendations via MCP protocol
- Server retrieves job listings (currently from local file, can use web scraping)
- Combines job data with user resume using AI prompt template
- Sends to DeepSeek API for intelligent matching
- Returns personalized job recommendations and advice

## How run the project
- First, we need to install necessary packages
- Then, prepare the data we need
- Setup environment variables via the .env file
- we use a local chromedriver to do web search, you should download it first

 chromedriver_path="/Users/fengshiyi/Downloads/chromedriver-mac-x64/chromedriver"

- Now, we can use args to specify the working directory and run the server:

```bash
uv --directory /Users/fengshiyi/Downloads/shayne/learning/LLM/py-projects/job-hunting-assistant/src/job_hunting_server run job-hunting-assistant
```


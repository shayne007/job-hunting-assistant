# Architecture Overview
This is a MCP (Model Context Protocol) server built with FastMCP framework that provides job hunting assistance through AI-powered job matching and recommendations.

## Key Components

- Entry Point (__init__.py, server.py)

    - Initializes the MCP server
    - Configures logging
    - Registers tools


- Core Server Layer (JobSearchMCPServer)

    - FastMCP-based server implementation
    - Tool registration and management
    - Request handling


- Business Logic Layer (JobTools)

    - Inherits from LLMClient for AI capabilities
    - Implements two main tools:

        - get_joblist_by_expect_job: Retrieves job listings
        - get_job_by_resume: Matches jobs with resumes




- Service Layer

    - LLM Integration: Uses DeepSeek API through OpenAI client
    - Web Scraping: Selenium-based BOSS直聘 scraper (currently disabled)
    - Prompt Management: Template-based prompt system


- Infrastructure Layer

    - Selenium WebDriver for web scraping
    - OpenAI client for LLM communication
    - File system for local data storage



## Data Flow

- Client requests job recommendations via MCP protocol
- Server retrieves job listings (currently from local file, can use web scraping)
- Combines job data with user resume using AI prompt template
- Sends to DeepSeek API for intelligent matching
- Returns personalized job recommendations and advice

# Current Implementation Notes

- Web scraping is disabled in favor of local file reading (job.txt)
- Uses DeepSeek API for AI processing
- Supports headless Chrome for web scraping when enabled
- Cookie-based authentication for BOSS直聘 access
- Template-based prompting for consistent AI interactions

The architecture follows a layered approach with clear separation of concerns, making it maintainable and extensible for future enhancements.
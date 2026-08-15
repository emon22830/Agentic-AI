from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.tools.tools import web_search, scrape_url


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# MODEL
# ============================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)


# ============================================================
# 1. SEARCH AGENT
# ============================================================

def build_search_agent():
    """
    Agent responsible for searching the web
    using the Tavily web_search tool.
    """

    return create_agent(
        model=llm,
        tools=[web_search],
    )


# ============================================================
# 2. READER AGENT
# ============================================================

def build_reader_agent():
    """
    Agent responsible for reading/scraping
    webpages using the scrape_url tool.
    """

    return create_agent(
        model=llm,
        tools=[scrape_url],
    )


# ============================================================
# 3. WRITER CHAIN
# ============================================================

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert research writer.

Your job is to write a clear, accurate and well-structured
research report based ONLY on the research provided.

Rules:
- Do not invent facts.
- Do not invent sources.
- Clearly explain important findings.
- Keep the writing professional and readable.
- Use the provided sources when making claims.
"""
    ),
    (
        "human",
        """
Write a detailed research report on the topic below.

Topic:
{topic}

Research Gathered:
{research}

Structure the report as:

1. Introduction

2. Key Findings
   - Finding 1
   - Finding 2
   - Finding 3
   - Add more findings if important.

3. Detailed Analysis

4. Conclusion

5. Sources
   - List all URLs found in the research.
"""
    ),
])


writer_chain = (
    writer_prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# 4. CRITIC CHAIN
# ============================================================

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a strict research critic.

Your job is to evaluate the quality of a research report.

Check for:

- Factual consistency
- Unsupported claims
- Missing important information
- Weak explanations
- Contradictions
- Poor source usage
- Whether the report answers the original topic
- Whether the conclusions are supported by the research

Do NOT rewrite the report.

Return your evaluation using this structure:

Overall Assessment:
PASS or NEEDS_IMPROVEMENT

Problems:
- ...

Missing Information:
- ...

Unsupported Claims:
- ...

Suggested Improvements:
- ...
"""
    ),
    (
        "human",
        """
Topic:
{topic}

Research:
{research}

Research Report:
{report}
"""
    ),
])


critic_chain = (
    critic_prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    topic = "Latest developments in AI research"

    # --------------------------------------------------------
    # Build agents
    # --------------------------------------------------------

    search_agent = build_search_agent()
    reader_agent = build_reader_agent()

    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    print("\n==============================")
    print("SEARCHING THE WEB")
    print("==============================\n")

    search_result = search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
Search the web for recent and reliable information
about: {topic}

Find several high-quality sources.
"""
            }
        ]
    })

    # Get the agent's final response
    search_output = search_result["messages"][-1].content

    print(search_output)

    # --------------------------------------------------------
    # Reader
    # --------------------------------------------------------

    print("\n==============================")
    print("READING SOURCES")
    print("==============================\n")

    reader_result = reader_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
Based on the search results below, identify useful URLs
and scrape the most relevant sources.

Search results:

{search_output}
"""
            }
        ]
    })

    research_output = reader_result["messages"][-1].content

    print(research_output)

    # --------------------------------------------------------
    # Writer
    # --------------------------------------------------------

    print("\n==============================")
    print("WRITING REPORT")
    print("==============================\n")

    report = writer_chain.invoke({
        "topic": topic,
        "research": research_output,
    })

    print(report)

    # --------------------------------------------------------
    # Critic
    # --------------------------------------------------------

    print("\n==============================")
    print("CRITIC REVIEW")
    print("==============================\n")

    critique = critic_chain.invoke({
        "topic": topic,
        "research": research_output,
        "report": report,
    })

    print(critique)

    # --------------------------------------------------------
    # Final output
    # --------------------------------------------------------

    print("\n==============================")
    print("RESEARCH COMPLETE")
    print("==============================\n")
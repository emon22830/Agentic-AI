from src.agents.agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain,
)


def research_pipeline(topic: str) -> str:

    state = {
        "topic": topic,
        "search_result": "",
        "research": "",
        "report": "",
        "critique": "",
    }

    # Step 1 — Search
    print("\n" + "=" * 60)
    print("STEP 1 — SEARCH AGENT")
    print("=" * 60)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
Search the web for recent and reliable information about:

{topic}

Find several high-quality sources.
"""
            }
        ]
    })

    state["search_result"] = search_result["messages"][-1].content

    # Step 2 — Reader
    print("\n" + "=" * 60)
    print("STEP 2 — READER AGENT")
    print("=" * 60)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
Based on these search results:

{state["search_result"]}

Identify the most relevant URLs and scrape them.
Return the useful research information.
"""
            }
        ]
    })

    state["research"] = reader_result["messages"][-1].content

    # Step 3 — Writer
    print("\n" + "=" * 60)
    print("STEP 3 — WRITER")
    print("=" * 60)

    state["report"] = writer_chain.invoke({
        "topic": state["topic"],
        "research": state["research"],
    })

    # Step 4 — Critic
    print("\n" + "=" * 60)
    print("STEP 4 — CRITIC")
    print("=" * 60)

    state["critique"] = critic_chain.invoke({
        "topic": state["topic"],
        "research": state["research"],
        "report": state["report"],
    })

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)

    return state["report"]
import streamlit as st

from src.pipelines.pipeline import research_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background-color: #0b1120;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background-color: #080d19;
        border-right: 1px solid #1e293b;
    }

    /* ---------- HEADERS ---------- */

    .brand {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        margin-top: 0.4rem;
        margin-bottom: 2rem;
    }

    /* ---------- CARDS ---------- */

    .card {
        background-color: #111827;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.4rem;
        margin-bottom: 1rem;
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .card-description {
        color: #94a3b8;
        font-size: 0.9rem;
    }

    /* ---------- PIPELINE ---------- */

    .step-number {
        color: #60a5fa;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .step-title {
        font-size: 1rem;
        font-weight: 700;
        margin-top: 0.3rem;
    }

    .step-description {
        color: #94a3b8;
        font-size: 0.82rem;
        margin-top: 0.3rem;
    }

    /* ---------- INPUT ---------- */

    div[data-testid="stTextInput"] input {
        background-color: #111827;
        border: 1px solid #334155;
        color: #f8fafc;
        border-radius: 10px;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        border-radius: 9px;
        min-height: 45px;
        font-weight: 600;
    }

    /* ---------- DIVIDER ---------- */

    hr {
        border-color: #1e293b;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        padding-top: 3rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🔎 ResearchFlow AI")

    st.caption("Multi-Agent Research Intelligence")

    st.divider()

    st.markdown("### Pipeline")

    st.markdown("""
    **01 · Search Agent**

    Finds recent web sources using Tavily.

    **02 · Reader Agent**

    Extracts readable content from webpages.

    **03 · Writer Chain**

    Synthesizes the research into a report.

    **04 · Critic Chain**

    Reviews the report for quality and gaps.
    """)

    st.divider()

    st.markdown("### Technology")

    st.markdown("""
    - LangChain
    - OpenAI
    - Tavily
    - BeautifulSoup
    - Trafilatura
    - Readability
    - Streamlit
    """)

    st.divider()

    st.caption("ResearchFlow AI")
    st.caption("Agentic Research System")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="brand">ResearchFlow AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'A multi-agent research workspace that searches, reads, '
    'synthesizes and critiques information.'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# PIPELINE OVERVIEW
# ============================================================

st.markdown("### Research pipeline")

cols = st.columns(4)

steps = [
    (
        "01",
        "Search Agent",
        "Discover relevant and recent sources.",
    ),
    (
        "02",
        "Reader Agent",
        "Extract useful information from webpages.",
    ),
    (
        "03",
        "Writer Chain",
        "Turn research into a structured report.",
    ),
    (
        "04",
        "Critic Chain",
        "Evaluate accuracy and research quality.",
    ),
]

for col, (number, title, description) in zip(cols, steps):

    with col:

        st.markdown(
            f"""
            <div class="card">
                <div class="step-number">{number}</div>
                <div class="step-title">{title}</div>
                <div class="step-description">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# RESEARCH INPUT
# ============================================================

st.markdown("### Start a research task")

topic = st.text_input(
    "Research topic",
    placeholder="e.g. How are AI agents changing software engineering?",
)

st.caption(
    "Enter a research question or topic. "
    "ResearchFlow will search the web and build a report."
)


# ============================================================
# EXAMPLE TOPICS
# ============================================================

st.markdown("##### Example topics")

example_cols = st.columns(3)

examples = [
    "Latest developments in AI research",
    "Future of multi-agent AI systems",
    "How AI agents are changing software engineering",
]

for col, example in zip(example_cols, examples):

    with col:

        if st.button(
            example,
            use_container_width=True,
        ):
            topic = example


# ============================================================
# START BUTTON
# ============================================================

st.markdown("")

start = st.button(
    "🚀  Start Research",
    type="primary",
    use_container_width=True,
)


# ============================================================
# RUN PIPELINE
# ============================================================

if start:

    if not topic.strip():

        st.warning(
            "Please enter a research topic before starting."
        )

    else:

        st.divider()

        st.markdown("### Research in progress")

        progress = st.progress(0)

        status = st.empty()

        try:

            # -----------------------------------------------
            # Search
            # -----------------------------------------------

            status.info(
                "🔍 Search Agent — discovering relevant sources..."
            )

            progress.progress(20)

            # -----------------------------------------------
            # Reader
            # -----------------------------------------------

            status.info(
                "📖 Reader Agent — analyzing webpages..."
            )

            progress.progress(45)

            # -----------------------------------------------
            # Writer
            # -----------------------------------------------

            status.info(
                "✍️ Writer Chain — synthesizing research..."
            )

            progress.progress(70)

            # -----------------------------------------------
            # Pipeline
            # -----------------------------------------------

            report = research_pipeline(topic)

            # -----------------------------------------------
            # Complete
            # -----------------------------------------------

            progress.progress(100)

            status.success(
                "Research completed successfully."
            )

            st.divider()

            # =================================================
            # REPORT
            # =================================================

            st.markdown("## Research Report")

            st.caption(
                f"Research topic: {topic}"
            )

            st.markdown(report)

            # =================================================
            # DOWNLOAD
            # =================================================

            st.divider()

            st.download_button(
                label="⬇️ Download Report",
                data=report,
                file_name="research_report.txt",
                mime="text/plain",
            )

        except Exception as e:

            progress.empty()

            status.error(
                "The research pipeline encountered an error."
            )

            st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div class="footer">'
    'ResearchFlow AI · Multi-Agent Research System'
    '</div>',
    unsafe_allow_html=True,
)
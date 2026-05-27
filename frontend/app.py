import streamlit as st
import requests
import os


BACKEND_URL = os.getenv(

    "BACKEND_URL",

    "http://127.0.0.1:8000/research"
)


st.set_page_config(

    page_title="AgentFlow API",

    layout="wide"
)


# =========================
# Session State
# =========================

if "history" not in st.session_state:

    st.session_state.history = []


if "selected_question" not in st.session_state:

    st.session_state.selected_question = ""


if "download_report" not in st.session_state:

    st.session_state.download_report = ""


# =========================
# Sidebar
# =========================

with st.sidebar:

    st.title("⚡ AgentFlow API")

    st.caption(
        "Multi-Agent Research Platform"
    )

    st.info(
        """
        Workflow:
        
        Query → Planner Agent
        → Retriever Agent
        → Research Agent
        → Fallback Logic
        """
    )

    st.divider()

    st.subheader(
        "📌 Sample Questions"
    )

    sample_questions = [

        "How are AI agents transforming enterprise automation?",

        "Applications of AI agents in business intelligence systems",

        "Future of multi-agent AI systems in healthcare and finance",

        "Challenges in building scalable multi-agent architectures",
    ]

    for q in sample_questions:

        if st.button(q):

            st.session_state.selected_question = q

    st.divider()

    st.subheader(
        "🕘 Run History"
    )

    if st.session_state.history:

        for idx, item in enumerate(
            st.session_state.history
        ):

            display_text = (

                item[:60] + "..."

                if len(item) > 60

                else item
            )

            if st.button(

                f"{idx + 1}. {display_text}",

                key=f"history_{idx}"
            ):

                st.session_state.selected_question = item

    else:

        st.info(
            "No research runs yet"
        )


# =========================
# Main UI
# =========================

st.title(
    "🧠 AgentFlow API — Multi-Agent Research Platform"
)


query = st.text_area(

    "Enter Research Query",

    value=st.session_state.selected_question,

    height=150
)


if st.button("Run Research"):

    if query:

        with st.spinner(

            "Planner Agent → Retriever Agent "
            "→ Research Agent running..."
        ):

            try:

                response = requests.post(

                    BACKEND_URL,

                    data={
                        "query": query
                    },

                    timeout=60
                )

                result = response.json()

                if not result.get("success"):

                    st.error(

                        result.get(
                            "error",
                            "Unknown error occurred"
                        )
                    )

                    st.stop()

                result = result["result"]

                # =========================
                # Save History
                # =========================

                st.session_state.history.insert(

                    0,

                    query
                )

                # =========================
                # Create Download Report
                # =========================

                report_text = f"""

Refined Query
--------------
{result["refined_query"]}


Retrieved Context
------------------
{result["retrieved_context"]}


Research Notes
---------------
{result["research_notes"]}


Final Answer
-------------
{result["final_answer"]}


Sources
--------
{result["sources"]}


Confidence
-----------
{result["confidence"]}
"""

                st.session_state.download_report = report_text

                # =========================
                # Display Results
                # =========================

                st.success(
                    "Research Completed"
                )

                # =========================
                # Metrics Row
                # =========================

                fallback_used = (

                    "Fallback response generated"

                    in result["research_notes"]
                )

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Documents Retrieved",
                    3
                )

                col2.metric(
                    "Confidence",
                    result["confidence"]
                )

                col3.metric(

                    "Fallback Used",

                    "Yes" if fallback_used else "No"
                )

                st.divider()

                # =========================
                # Refined Query
                # =========================

                with st.container(border=True):

                    st.subheader(
                        "Refined Query"
                    )

                    st.write(
                        result["refined_query"]
                    )

                # =========================
                # Retrieved Context
                # =========================

                with st.container(border=True):

                    st.subheader(
                        "Retrieved Context"
                    )

                    with st.expander(
                        "View Retrieved Context"
                    ):

                        st.write(
                            result["retrieved_context"]
                        )

                # =========================
                # Research Notes
                # =========================

                with st.container(border=True):

                    st.subheader(
                        "Research Notes"
                    )

                    st.write(
                        result["research_notes"]
                    )

                # =========================
                # Final Answer
                # =========================

                with st.container(border=True):

                    st.subheader(
                        "Final Answer"
                    )

                    st.write(
                        result["final_answer"]
                    )

                # =========================
                # Sources
                # =========================

                with st.container(border=True):

                    st.subheader(
                        "Sources"
                    )

                    with st.expander(
                        "View Sources"
                    ):

                        st.write(
                            result["sources"]
                        )

                # =========================
                # Confidence
                # =========================

                with st.container(border=True):

                    st.subheader(
                        "Confidence"
                    )

                    confidence = result["confidence"]

                    if confidence == "High":

                        st.success(
                            "High Confidence"
                        )

                    elif confidence == "Medium":

                        st.warning(
                            "Medium Confidence"
                        )

                    else:

                        st.error(
                            "Low Confidence"
                        )

                # =========================
                # Download Report
                # =========================

                st.divider()

                st.subheader(
                    "⬇ Download Report"
                )

                if st.session_state.download_report:

                    st.download_button(

                        label="Download Latest Report",

                        data=st.session_state.download_report,

                        file_name="research_report.txt",

                        mime="text/plain"
                    )

                else:

                    st.info(
                        "Run research first"
                    )

            except Exception as e:

                st.error(
                    f"Frontend error: {e}"
                )
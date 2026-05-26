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

            if st.button(

                f"{idx + 1}. {item}",

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
            "Running multi-agent workflow..."
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

                st.subheader(
                    "Refined Query"
                )

                st.write(
                    result["refined_query"]
                )

                st.subheader(
                    "Retrieved Context"
                )

                st.write(
                    result["retrieved_context"]
                )

                st.subheader(
                    "Research Notes"
                )

                st.write(
                    result["research_notes"]
                )

                st.subheader(
                    "Final Answer"
                )

                st.write(
                    result["final_answer"]
                )

                st.subheader(
                    "Confidence"
                )

                st.write(
                    result["confidence"]
                )

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
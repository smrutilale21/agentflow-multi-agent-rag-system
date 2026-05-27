from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from graph import build_graph
from logger import setup_logger

logger = setup_logger()

app = FastAPI(title="AgentFlow API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():

    logger.info("Health check endpoint called")

    return {"status": "running"}


@app.post("/research")
async def research(query: str = Form(...)):

    try:

        logger.info(f"Received query: {query}")

        graph = build_graph()

        result = graph.invoke(
            {
                "user_query": query,
                "refined_query": "",
                "retrieved_context": "",
                "research_notes": "",
                "sources": "",
                "final_answer": "",
                "confidence": "",
            }
        )

        logger.info("Research completed successfully")

        return {"success": True, "result": result}

    except Exception as e:

        logger.error(f"Research endpoint failed: {e}")

        return {"success": False, "error": str(e)}

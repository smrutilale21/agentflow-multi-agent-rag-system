import os

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import get_openai_api_key
from logger import setup_logger
from pypdf import PdfReader


logger = setup_logger()

CHROMA_DIR = "chroma_db"

COLLECTION_NAME = "research_knowledge_base"

DATA_DIR = "../data"


def load_knowledge_base() -> list[dict]:

    if not os.path.exists(DATA_DIR):

        raise FileNotFoundError(
            f"{DATA_DIR} directory not found."
        )

    documents = []

    pdf_files = [

        file

        for file in os.listdir(DATA_DIR)

        if file.endswith(".pdf")
    ]

    if not pdf_files:

        raise FileNotFoundError(
            "No PDF files found in data directory."
        )

    for pdf_file in pdf_files:

        file_path = os.path.join(
            DATA_DIR,
            pdf_file
        )

        logger.info(
            f"Loading PDF: {pdf_file}"
        )

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted + "\n"

        documents.append({

            "source": pdf_file,

            "content": text
        })

    logger.info(
        f"Loaded {len(documents)} PDF files"
    )

    return documents


def create_documents(
    knowledge_base: list[dict]
) -> list[Document]:

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=800,

        chunk_overlap=100
    )

    documents = []

    for knowledge in knowledge_base:

        source = knowledge["source"]

        content = knowledge["content"]

        chunks = splitter.split_text(content)

        for index, chunk in enumerate(chunks):

            documents.append(

                Document(

                    page_content=chunk,

                    metadata={

                        "source": source,

                        "chunk_id": index
                    }
                )
            )

    logger.info(
        f"Created {len(documents)} chunks"
    )

    return documents


def get_embeddings() -> OpenAIEmbeddings:

    return OpenAIEmbeddings(

        model="text-embedding-3-small",

        api_key=get_openai_api_key()
    )


def get_vector_store() -> Chroma:

    embeddings = get_embeddings()

    vector_store = Chroma(

        collection_name=COLLECTION_NAME,

        persist_directory=CHROMA_DIR,

        embedding_function=embeddings,
    )

    existing_count = vector_store._collection.count()

    if existing_count > 0:

        logger.info(

            f"Loaded existing Chroma collection with "
            f"{existing_count} documents"
        )

        return vector_store

    logger.info(
        "Creating new Chroma vector store"
    )

    knowledge_base = load_knowledge_base()

    documents = create_documents(
        knowledge_base
    )

    vector_store.add_documents(documents)

    logger.info(
        f"Added {len(documents)} chunks to Chroma"
    )

    return vector_store
from langchain_community.vectorstores import FAISS

from app.rag.loader import load_documents
from app.rag.embeddings import get_embeddings


def build_vector_store():
    docs = load_documents()

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        docs,
        embeddings,
    )

    vectorstore.save_local("faiss_index")

    return vectorstore
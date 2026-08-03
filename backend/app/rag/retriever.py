from langchain_community.vectorstores import FAISS

from app.rag.embeddings import get_embeddings


def get_retriever():

    embeddings = get_embeddings()

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5},
    )


def search(query: str):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    print("\n========== RAG RETRIEVAL ==========\n")

    for i, doc in enumerate(docs, 1):
        print(f"\nDocument {i}\n")
        print(doc.page_content)
        print("-" * 60)

    return docs
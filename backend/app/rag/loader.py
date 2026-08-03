from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader


KNOWLEDGE_PATH = Path(__file__).resolve().parents[2] / "knowledge"


def load_documents():
    documents = []

    for folder in KNOWLEDGE_PATH.iterdir():
        if folder.is_dir():
            loader = DirectoryLoader(
                str(folder),
                glob="**/*.txt",
                loader_cls=TextLoader,
            )

            documents.extend(loader.load())

    return documents
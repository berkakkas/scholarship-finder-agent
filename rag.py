from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings
import os
import hashlib


class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [self._embed_text(text) for text in texts]

    def embed_query(self, text):
        return self._embed_text(text)

    def _embed_text(self, text):
        vector = [0.0] * 64
        words = text.lower().split()

        for word in words:
            index = int(hashlib.md5(word.encode()).hexdigest(), 16) % 64
            vector[index] += 1.0

        return vector


def load_documents():
    docs = []
    folder = "docs"

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)
            loader = TextLoader(path, encoding="utf-8")
            loaded_docs = loader.load()

            for doc in loaded_docs:
                if doc.page_content.strip():
                    docs.append(doc)

    return docs


def create_vector_store():
    docs = load_documents()

    if not docs:
        raise ValueError("docs folder has no valid .txt documents. Add at least one non-empty txt file.")

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=SimpleEmbeddings(),
        persist_directory="chroma_db"
    )

    return vectorstore


def search_documents(query):
    vectorstore = create_vector_store()
    results = vectorstore.similarity_search(query, k=3)

    return "\n".join([doc.page_content for doc in results])
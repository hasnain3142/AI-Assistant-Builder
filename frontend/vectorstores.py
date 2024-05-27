import os
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, StorageContext, ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient, AsyncQdrantClient
import GlobalConstants
import nest_asyncio

nest_asyncio.apply()
os.environ["OPENAI_API_KEY"] = GlobalConstants.OPENAI_KEY

class VectorDB:
    def __init__(self):
        self.index = None

    def create_index(self, collection_name=""):
        aclient = AsyncQdrantClient(host="localhost", port=6333)
        client = QdrantClient(host="localhost", port=6333)

        # create our vector store with hybrid indexing enabled
        # batch_size controls how many nodes are encoded with sparse vectors at once
        vector_store = QdrantVectorStore(collection_name=collection_name, client=client, aclient=aclient, enable_hybrid=True, batch_size=20)

        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        Settings.chunk_size = 512
        documents = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model=GlobalConstants.MODEL, temperature=0.5, system_prompt=GlobalConstants.PROMPT))
        self.index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, use_async=True)
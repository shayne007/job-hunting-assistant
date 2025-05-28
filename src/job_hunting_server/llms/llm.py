import os
import logging
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import  DashScopeEmbeddings
from langchain_qdrant import QdrantVectorStore


def DeepSeek():
    return ChatOpenAI(
        model="deepseek-chat",
        api_key=os.environ.get("deepseek"),  # 自行搞定  你的秘钥
        base_url="https://api.deepseek.com"
    )
def DeepSeekR1():
    return ChatOpenAI(
        model="deepseek-reasoner",
        api_key=os.environ.get("deepseek"),  # 自行搞定  你的秘钥
        base_url="https://api.deepseek.com"
    )
def TongyiEmbedding()->DashScopeEmbeddings:
    api_key=os.environ.get("dashscope")
    return DashScopeEmbeddings(dashscope_api_key=api_key,
                           model="text-embedding-v1")

def QdrantVecStoreFromDocs(docs:List[Document]):
    eb=TongyiEmbedding()
    return QdrantVectorStore.from_documents(docs,eb,url="http://localhost:6333")

def QdrantVecStore(eb:DashScopeEmbeddings,collection_name:str):
    return  QdrantVectorStore.\
        from_existing_collection(embedding=eb,
         url="http://localhost:6333",
          collection_name=collection_name)

class LLMClient:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.client = self._get_client()

    def _get_client(self)->OpenAI:
        load_dotenv()

        client = OpenAI(
            #api_key=os.getenv("AliDeep"),  
            #base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
            api_key=os.getenv("deepseek"),
            base_url="https://api.deepseek.com"
        )

        return client

    def send_messages(self, messages):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
        )
        return response
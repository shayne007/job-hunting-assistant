from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from job_hunting_server.llms.llm import QdrantVecStoreFromDocs, DeepSeek
from job_hunting_server.prompts.prompt import RAGPrompt
from langchain import hub
import nltk
import os
from pathlib import Path

def clearstr(s):
    filter_chars = ['\n', '\r', '\t', '\u3000','  ']
    for char in filter_chars:
        s=s.replace(char,'')
    return s

def format_docs(docs):
    return "\n\n".join(clearstr(doc.page_content) for doc in docs)

def load_doc(doc_path=None) -> str:
    try:
        # Download required NLTK data
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)

        # Use provided path or default path
        if doc_path is None:
            doc_path = os.path.join(os.path.dirname(__file__), '../../../data/简历.docx')
        
        if not os.path.exists(doc_path):
            raise FileNotFoundError(f"Document not found at path: {doc_path}")

        word = UnstructuredWordDocumentLoader(doc_path)
        docs = word.load()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=50,
            chunk_overlap=20
        )
        s_docs = splitter.split_documents(docs)
        
        vec_store = QdrantVecStoreFromDocs(s_docs)
        llm = DeepSeek()
        
        # read from local or pull from hub
        prompt = hub.pull("rlm/rag-prompt")
        chain = (
            {"context": vec_store.as_retriever() | format_docs,
             "question": RunnablePassthrough()} 
            | prompt 
            | llm 
            | StrOutputParser()
        )
        
        ret = chain.invoke("请输出姓名.格式如下\n姓名: ?")
        print(ret)
        summary=ret
        ret = chain.invoke("总结专业技能情况,内容可能包含Java、AI Agent、python、rag等.格式如下\n专业技能: ?")
        print(ret)
        summary+=ret
        ret = chain.invoke("根据各大公司工作过的项目经历总结.格式如下\n项目经验: ")
        print(ret)
        summary+=ret
        return summary
    except Exception as e:
        print(f"Error processing document: {str(e)}")
        raise

if __name__ == '__main__':
    load_doc()
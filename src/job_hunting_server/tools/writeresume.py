from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

from job_hunting_server.llms.llm import DeepSeekR1
from job_hunting_server.prompts.prompt import ResumePrompt,ResumePrompt2

# 加载 职位描述
def load_jobs() -> str:
    with open(f'/Users/fengshiyi/Downloads/shayne/learning/LLM/py-projects/job-hunting-assistant/data/job_desc.txt', 'r', encoding='utf-8') as f:
        jobs=f.read()
    
    return jobs

def load_doc() -> list:
    word=UnstructuredWordDocumentLoader('/Users/fengshiyi/Downloads/shayne/learning/LLM/py-projects/job-hunting-assistant/data/简历.docx')
    docs=word.load()

    return docs

def write_resume():
    prompt=PromptTemplate.from_template(ResumePrompt)
    llm=DeepSeekR1()
    chain={
        "input":RunnablePassthrough()
    } | prompt | llm | StrOutputParser()
    ret=chain.invoke(load_jobs())
    print(ret)

def fix_resume(resume_content: str,target_job: str) -> str:
    prompt=PromptTemplate.from_template(ResumePrompt2)
    llm=DeepSeekR1()
    doc = resume_content
    if(doc == None):
        doc=load_doc()
    chain={
        "resume": lambda _: doc,
        "input":RunnablePassthrough()
    } | prompt | llm | StrOutputParser()
    input = target_job
    if(input == None):
        input = load_jobs()
    ret=chain.invoke(input)
    print(ret)
    return ret

if __name__ == '__main__':
    fix_resume()
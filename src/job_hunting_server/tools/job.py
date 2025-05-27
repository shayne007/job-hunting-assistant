from typing import Any
from ..llms.llm import LLMClient 
from ..prompts.prompt import Job_Search_Prompt
from ..selenium.listjob import listjob_by_keyword

class JobTools(LLMClient):
    def register_tools(self, mcp: Any):
        """Register job tools."""
        @mcp.tool(description="根据求职者的期望岗位获取岗位列表数据")
        def get_joblist_by_expect_job(job: str) -> str:
            """根据求职者的期望岗位获取岗位列表数据"""
            # 为了测试方便，可以改成从本地文件获取岗位列表
            with open('job.txt', 'r', encoding='utf-8') as f:
                jobs = f.read()
            
            #使用无头浏览器获取岗位
            # jobs = listjob_by_keyword(job)

            return jobs

        @mcp.tool(description="根据岗位列表以及求职者的简历获取适合该求职者的岗位以及求职建议")
        def get_job_by_resume(jobs: str, resume: str) -> str:
            """根据岗位列表以及求职者的简历获取适合该求职者的岗位以及求职建议"""
            #将简历以及岗位列表注入到 prompt 模板
            prompt = Job_Search_Prompt.format(resume=resume,job_list=jobs)
            messages = [{"role": "user", "content": prompt}]
            
            self.logger.info(f"prompt: {prompt}")

            #发送给 ds
            response = LLMClient.send_messages(self,messages)
            response_text = response.choices[0].message.content

            return response_text
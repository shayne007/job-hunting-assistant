from typing import Any
from ..word.word import read_word_file
from ..word.loaddoc import load_doc
from ..tools.writeresume import fix_resume
class ResumeTools():
    def register_tools(self, mcp: Any):
        """Register job tools."""

        @mcp.tool(description="读取指定路径的word文件")
        def get_word_by_filepath(filepath: str) -> list:
            """根据文件路径获取word文件内容"""
            # content=read_word_file(filepath)
            content = load_doc(filepath)
            return content
        @mcp.tool(description="根据简历内容和目标岗位描述，进行简历优化")
        def fix_resume_by_target_job(resume_content: str,target_job: str) -> list:
            """根据简历内容和目标岗位描述，进行简历优化"""
            content = fix_resume(resume_content,target_job)
            return content
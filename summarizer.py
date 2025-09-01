from openai import OpenAI
from typing import Dict, List
import config

class PaperSummarizer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or config.OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("需要提供OpenAI API密钥")
        
        self.client = OpenAI(api_key=self.api_key)
    
    def summarize_paper(self, paper: Dict, language: str = "chinese") -> str:
        """
        为单篇论文生成总结
        
        Args:
            paper: 论文信息字典
            language: 总结语言 ("chinese" 或 "english")
            
        Returns:
            论文总结
        """
        title = paper['title']
        abstract = paper['abstract']
        
        if language == "chinese":
            prompt = f"""
请为以下学术论文生成一个简洁的中文总结（不超过150字）：

标题：{title}

摘要：{abstract}

请用中文总结这篇论文的：
1. 主要研究内容
2. 核心方法或贡献
3. 实际应用价值

总结要简洁明了，适合快速了解论文要点。
"""
        else:
            prompt = f"""
Please provide a concise summary (no more than 150 words) for the following academic paper:

Title: {title}

Abstract: {abstract}

Please summarize:
1. Main research content
2. Key methods or contributions  
3. Practical application value

Keep the summary concise and suitable for quick understanding.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一个专业的学术论文总结助手。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.3
            )
            
            summary = response.choices[0].message.content.strip()
            return summary
            
        except Exception as e:
            print(f"生成总结时出错: {e}")
            return f"无法生成总结: {str(e)}"
    
    def summarize_papers(self, papers: List[Dict], language: str = "chinese") -> List[Dict]:
        """
        为多篇论文生成总结
        
        Args:
            papers: 论文信息列表
            language: 总结语言
            
        Returns:
            包含总结的论文信息列表
        """
        summarized_papers = []
        
        for i, paper in enumerate(papers, 1):
            print(f"正在生成第 {i}/{len(papers)} 篇论文的总结...")
            
            paper_copy = paper.copy()
            paper_copy['summary'] = self.summarize_paper(paper, language)
            summarized_papers.append(paper_copy)
        
        return summarized_papers
#!/usr/bin/env python3
"""
arXiv论文获取模块 / arXiv Paper Fetching Module
负责从arXiv搜索和获取论文信息 / Responsible for searching and fetching paper information from arXiv
"""

import arxiv
import feedparser
from datetime import datetime, timedelta
from typing import List, Dict
import re

class ArxivFetcher:
    """
    arXiv论文获取器 / arXiv Paper Fetcher
    用于搜索和获取arXiv上的学术论文 / Used to search and fetch academic papers from arXiv
    """
    
    def __init__(self, max_results: int = 10):
        """
        初始化获取器 / Initialize the fetcher
        
        Args:
            max_results (int): 最大结果数量 / Maximum number of results
        """
        self.max_results = max_results
        self.client = arxiv.Client()
    
    def search_papers(self, keywords: List[str], days_back: int = 1) -> List[Dict]:
        """
        根据关键词搜索arXiv论文 / Search arXiv papers by keywords
        
        Args:
            keywords: 搜索关键词列表 / List of search keywords
            days_back: 搜索最近几天的论文 / Search papers from recent days
            
        Returns:
            论文信息列表 / List of paper information
        """
        # 构建搜索查询 / Build search query
        query_parts = []
        for keyword in keywords:
            # 在标题、摘要和关键词中搜索 / Search in title, abstract and keywords
            query_parts.append(f'(ti:"{keyword}" OR abs:"{keyword}")')
        
        query = " OR ".join(query_parts)
        
        # 创建搜索对象
        search = arxiv.Search(
            query=query,
            max_results=self.max_results * 2,  # 获取更多结果以便筛选
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        
        papers = []
        cutoff_date = datetime.now() - timedelta(days=days_back)
        
        try:
            for paper in self.client.results(search):
                # 检查论文提交日期
                if paper.published.replace(tzinfo=None) < cutoff_date:
                    continue
                
                paper_info = {
                    'title': paper.title,
                    'authors': [str(author) for author in paper.authors],
                    'abstract': paper.summary,
                    'url': paper.entry_id,
                    'pdf_url': paper.pdf_url,
                    'published': paper.published.strftime('%Y-%m-%d'),
                    'categories': paper.categories
                }
                papers.append(paper_info)
                
                if len(papers) >= self.max_results:
                    break
                    
        except Exception as e:
            print(f"搜索论文时出错: {e}")
            return []
        
        return papers
    
    def clean_text(self, text: str) -> str:
        """清理文本，移除多余的空白字符和换行符"""
        # 移除多余的空白字符和换行符
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def format_authors(self, authors: List[str], max_authors: int = 3) -> str:
        """格式化作者列表"""
        if len(authors) <= max_authors:
            return ", ".join(authors)
        else:
            return ", ".join(authors[:max_authors]) + f" et al. ({len(authors)} authors)"
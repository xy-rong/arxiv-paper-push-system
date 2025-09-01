#!/usr/bin/env python3
"""
arXiv 论文推送系统 - 演示版本
不需要OpenAI API，使用论文摘要作为总结
"""

import argparse
from typing import List
from datetime import datetime

from arxiv_fetcher import ArxivFetcher
from report_generator import ReportGenerator
import config

class ArxivPusherDemo:
    def __init__(self):
        self.fetcher = ArxivFetcher(max_results=config.MAX_RESULTS)
        self.reporter = ReportGenerator()
    
    def process_papers_with_abstract_summary(self, papers: List[dict]) -> List[dict]:
        """使用论文摘要作为总结（截取前200字符）"""
        for paper in papers:
            abstract = paper['abstract']
            # 清理并截取摘要
            clean_abstract = self.fetcher.clean_text(abstract)
            if len(clean_abstract) > 200:
                summary = clean_abstract[:200] + "..."
            else:
                summary = clean_abstract
            paper['summary'] = summary
        return papers
    
    def fetch_and_process(self, keywords: List[str], days_back: int = 1, 
                         output_format: str = "html", save_file: bool = True) -> List[dict]:
        """获取并处理论文"""
        
        print(f"🔍 正在搜索关键词: {', '.join(keywords)}")
        print(f"📅 搜索最近 {days_back} 天的论文...")
        
        # 获取论文
        papers = self.fetcher.search_papers(keywords, days_back)
        
        if not papers:
            print("❌ 未找到相关论文")
            return []
        
        print(f"📚 找到 {len(papers)} 篇相关论文")
        
        # 使用摘要作为总结
        papers = self.process_papers_with_abstract_summary(papers)
        
        # 生成报告
        if save_file:
            report_path = self.reporter.save_report(papers, keywords, output_format)
            print(f"📄 报告已保存到: {report_path}")
        
        # 在控制台显示
        self.reporter.print_console_report(papers, keywords)
        
        return papers
    
    def run_once(self, keywords: List[str], days_back: int = 1, 
                output_format: str = "html", save_file: bool = True):
        """运行一次推送"""
        try:
            papers = self.fetch_and_process(keywords, days_back, output_format, save_file)
            print(f"\n✅ 推送完成! 处理了 {len(papers)} 篇论文")
        except Exception as e:
            print(f"❌ 推送过程中出错: {e}")

def main():
    parser = argparse.ArgumentParser(description="arXiv 论文推送系统 - 演示版本")
    parser.add_argument(
        "--keywords", "-k", 
        nargs="+", 
        default=config.DEFAULT_KEYWORDS,
        help="搜索关键词"
    )
    parser.add_argument(
        "--days", "-d", 
        type=int, 
        default=config.DAYS_BACK,
        help="搜索最近几天的论文 (默认: 1)"
    )
    parser.add_argument(
        "--format", "-f", 
        choices=["html", "markdown"], 
        default="html",
        help="输出格式 (默认: html)"
    )
    parser.add_argument(
        "--no-save", 
        action="store_true",
        help="不保存报告文件，只在控制台显示"
    )
    
    args = parser.parse_args()
    
    # 创建推送器
    pusher = ArxivPusherDemo()
    
    # 单次运行模式
    pusher.run_once(
        keywords=args.keywords,
        days_back=args.days,
        output_format=args.format,
        save_file=not args.no_save
    )

if __name__ == "__main__":
    main()
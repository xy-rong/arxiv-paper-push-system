#!/usr/bin/env python3
"""
arXiv 论文推送系统
根据关键词每天推送相关论文并生成总结
"""

import argparse
import sys
from typing import List
import schedule
import time
from datetime import datetime

from arxiv_fetcher import ArxivFetcher
from summarizer import PaperSummarizer
from report_generator import ReportGenerator
import config

class ArxivPusher:
    def __init__(self):
        self.fetcher = ArxivFetcher(max_results=config.MAX_RESULTS)
        self.summarizer = None
        self.reporter = ReportGenerator()
        
        # 初始化总结器（如果有API密钥）
        if config.OPENAI_API_KEY:
            try:
                self.summarizer = PaperSummarizer()
                print("✅ OpenAI API 已配置，将生成论文总结")
            except Exception as e:
                print(f"⚠️  OpenAI API 配置失败: {e}")
                print("📝 将跳过总结生成功能")
        else:
            print("⚠️  未配置 OpenAI API 密钥，将跳过总结生成功能")
    
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
        
        # 生成总结
        if self.summarizer:
            print("🤖 正在生成论文总结...")
            papers = self.summarizer.summarize_papers(
                papers, 
                language=config.SUMMARY_LANGUAGE
            )
            print("✅ 总结生成完成")
        
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
    
    def schedule_daily_push(self, keywords: List[str], time_str: str = "09:00"):
        """安排每日定时推送"""
        print(f"⏰ 已安排每日 {time_str} 自动推送")
        print(f"🔍 搜索关键词: {', '.join(keywords)}")
        print("按 Ctrl+C 停止定时任务")
        
        schedule.every().day.at(time_str).do(
            self.run_once, 
            keywords=keywords,
            days_back=config.DAYS_BACK,
            output_format="html",
            save_file=True
        )
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # 每分钟检查一次
        except KeyboardInterrupt:
            print("\n⏹️  定时任务已停止")

def main():
    parser = argparse.ArgumentParser(description="arXiv 论文推送系统")
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
        "--schedule", "-s", 
        type=str,
        help="定时推送时间，格式: HH:MM (如: 09:00)"
    )
    parser.add_argument(
        "--no-save", 
        action="store_true",
        help="不保存报告文件，只在控制台显示"
    )
    
    args = parser.parse_args()
    
    # 创建推送器
    pusher = ArxivPusher()
    
    if args.schedule:
        # 定时推送模式
        pusher.schedule_daily_push(args.keywords, args.schedule)
    else:
        # 单次运行模式
        pusher.run_once(
            keywords=args.keywords,
            days_back=args.days,
            output_format=args.format,
            save_file=not args.no_save
        )

if __name__ == "__main__":
    main()
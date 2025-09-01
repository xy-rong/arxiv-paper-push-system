from typing import List, Dict
from datetime import datetime
import os

class ReportGenerator:
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_html_report(self, papers: List[Dict], keywords: List[str]) -> str:
        """生成HTML格式的报告"""
        
        html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>arXiv 论文日报 - {datetime.now().strftime('%Y-%m-%d')}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 20px;
        }}
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .keywords {{
            background-color: #e8f5e8;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}
        .paper {{
            margin-bottom: 30px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #fafafa;
        }}
        .paper-title {{
            font-size: 1.3em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .paper-authors {{
            color: #7f8c8d;
            margin-bottom: 10px;
            font-style: italic;
        }}
        .paper-info {{
            margin-bottom: 15px;
            font-size: 0.9em;
            color: #666;
        }}
        .paper-summary {{
            background-color: white;
            padding: 15px;
            border-left: 4px solid #4CAF50;
            margin: 15px 0;
        }}
        .paper-links {{
            margin-top: 15px;
        }}
        .paper-links a {{
            display: inline-block;
            margin-right: 15px;
            padding: 8px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.9em;
        }}
        .paper-links a:hover {{
            background-color: #45a049;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 arXiv 论文日报</h1>
            <p>日期: {datetime.now().strftime('%Y年%m月%d日')}</p>
        </div>
        
        <div class="keywords">
            <strong>🔍 搜索关键词:</strong> {', '.join(keywords)}
        </div>
        
        <div class="papers">
"""
        
        for i, paper in enumerate(papers, 1):
            html_content += f"""
            <div class="paper">
                <div class="paper-title">
                    {i}. {paper['title']}
                </div>
                <div class="paper-authors">
                    👥 作者: {', '.join(paper['authors'][:3])}{'等' if len(paper['authors']) > 3 else ''}
                </div>
                <div class="paper-info">
                    📅 发布日期: {paper['published']} | 🏷️ 分类: {', '.join(paper['categories'])}
                </div>
                <div class="paper-summary">
                    <strong>📝 总结:</strong><br>
                    {paper.get('summary', '暂无总结')}
                </div>
                <div class="paper-links">
                    <a href="{paper['url']}" target="_blank">📄 查看论文</a>
                    <a href="{paper['pdf_url']}" target="_blank">📥 下载PDF</a>
                </div>
            </div>
"""
        
        html_content += f"""
        </div>
        
        <div class="footer">
            <p>📊 共找到 {len(papers)} 篇相关论文</p>
            <p>🤖 由 arXiv 论文推送系统自动生成</p>
        </div>
    </div>
</body>
</html>
"""
        
        return html_content
    
    def generate_markdown_report(self, papers: List[Dict], keywords: List[str]) -> str:
        """生成Markdown格式的报告"""
        
        md_content = f"""# 📚 arXiv 论文日报

**日期:** {datetime.now().strftime('%Y年%m月%d日')}  
**搜索关键词:** {', '.join(keywords)}  
**论文数量:** {len(papers)}

---

"""
        
        for i, paper in enumerate(papers, 1):
            authors_str = ', '.join(paper['authors'][:3])
            if len(paper['authors']) > 3:
                authors_str += '等'
            
            md_content += f"""## {i}. {paper['title']}

**👥 作者:** {authors_str}  
**📅 发布日期:** {paper['published']}  
**🏷️ 分类:** {', '.join(paper['categories'])}

**📝 总结:**  
{paper.get('summary', '暂无总结')}

**🔗 链接:**  
- [查看论文]({paper['url']})  
- [下载PDF]({paper['pdf_url']})

---

"""
        
        return md_content
    
    def save_report(self, papers: List[Dict], keywords: List[str], format: str = "html") -> str:
        """保存报告到文件"""
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if format.lower() == "html":
            content = self.generate_html_report(papers, keywords)
            filename = f"arxiv_report_{timestamp}.html"
        else:
            content = self.generate_markdown_report(papers, keywords)
            filename = f"arxiv_report_{timestamp}.md"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def print_console_report(self, papers: List[Dict], keywords: List[str]):
        """在控制台打印报告"""
        
        print("=" * 80)
        print(f"📚 arXiv 论文日报 - {datetime.now().strftime('%Y年%m月%d日')}")
        print("=" * 80)
        print(f"🔍 搜索关键词: {', '.join(keywords)}")
        print(f"📊 找到论文数量: {len(papers)}")
        print("=" * 80)
        
        for i, paper in enumerate(papers, 1):
            print(f"\n{i}. {paper['title']}")
            print(f"   👥 作者: {', '.join(paper['authors'][:3])}{'等' if len(paper['authors']) > 3 else ''}")
            print(f"   📅 发布: {paper['published']} | 🏷️ 分类: {', '.join(paper['categories'])}")
            print(f"   📝 总结: {paper.get('summary', '暂无总结')}")
            print(f"   🔗 链接: {paper['url']}")
            print("-" * 80)
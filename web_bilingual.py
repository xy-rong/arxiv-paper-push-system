#!/usr/bin/env python3
"""
arXiv 论文推送系统 - 双语Web版本 / arXiv Paper Push System - Bilingual Web Version
支持中英文界面切换的Web应用 / Web application with Chinese-English interface switching
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import threading
import os
import tempfile
from datetime import datetime
from typing import List, Dict
import json

from arxiv_fetcher import ArxivFetcher
from summarizer import PaperSummarizer
from report_generator import ReportGenerator
import config

app = Flask(__name__)
CORS(app)

# 全局变量 / Global variables
fetcher = ArxivFetcher(max_results=config.MAX_RESULTS)
summarizer = None
reporter = ReportGenerator()

# 检查OpenAI API / Check OpenAI API
has_openai_api = bool(config.OPENAI_API_KEY)
if has_openai_api:
    try:
        summarizer = PaperSummarizer()
    except Exception as e:
        has_openai_api = False
        print(f"OpenAI API 初始化失败 / OpenAI API initialization failed: {e}")

# 搜索状态 / Search status
search_status = {
    'is_searching': False,
    'progress': 0,
    'message': '准备就绪 / Ready',
    'papers': []
}

@app.route('/')
def index():
    """主页 / Main page"""
    return render_template('bilingual.html', has_openai_api=has_openai_api)

@app.route('/api/search', methods=['POST'])
def search_papers():
    """搜索论文API / Search papers API"""
    global search_status
    
    if search_status['is_searching']:
        return jsonify({'error': '搜索正在进行中 / Search in progress'}), 400
    
    data = request.json
    keywords_text = data.get('keywords', '').strip()
    
    if not keywords_text:
        return jsonify({'error': '请输入搜索关键词 / Please enter search keywords'}), 400
    
    keywords = [k.strip() for k in keywords_text.split(',') if k.strip()]
    days = int(data.get('days', 7))
    count = int(data.get('count', 10))
    language = data.get('language', 'chinese')
    
    # 重置状态 / Reset status
    search_status.update({
        'is_searching': True,
        'progress': 0,
        'message': '开始搜索... / Starting search...',
        'papers': []
    })
    
    # 更新fetcher的最大结果数 / Update fetcher max results
    fetcher.max_results = count
    
    # 在新线程中执行搜索 / Execute search in new thread
    search_thread = threading.Thread(
        target=perform_search,
        args=(keywords, days, language),
        daemon=True
    )
    search_thread.start()
    
    return jsonify({'message': '搜索已开始 / Search started'})

def perform_search(keywords: List[str], days: int, language: str):
    """执行搜索的后台任务 / Background task for performing search"""
    global search_status
    
    try:
        # 更新状态 / Update status
        search_status.update({
            'progress': 10,
            'message': f'🔍 正在搜索关键词 / Searching keywords: {", ".join(keywords)}'
        })
        
        # 搜索论文 / Search papers
        papers = fetcher.search_papers(keywords, days)
        
        if not search_status['is_searching']:
            return
        
        if not papers:
            search_status.update({
                'is_searching': False,
                'progress': 0,
                'message': '❌ 未找到相关论文 / No relevant papers found',
                'papers': []
            })
            return
        
        search_status.update({
            'progress': 50,
            'message': f'📚 找到 {len(papers)} 篇论文，正在处理摘要... / Found {len(papers)} papers, processing abstracts...'
        })
        
        # 使用摘要作为总结 / Use abstracts as summaries
        for i, paper in enumerate(papers):
            if not search_status['is_searching']:
                return
            
            abstract = paper['abstract']
            clean_abstract = fetcher.clean_text(abstract)
            
            # 根据语言处理摘要 / Process abstract based on language
            if language == 'chinese':
                if len(clean_abstract) > 200:
                    summary = clean_abstract[:200] + "..."
                else:
                    summary = clean_abstract
                summary = f"【论文摘要】{summary}"
            else:
                if len(clean_abstract) > 300:
                    summary = clean_abstract[:300] + "..."
                else:
                    summary = clean_abstract
                summary = f"[Abstract] {summary}"
            
            paper['summary'] = summary
            
            # 更新进度 / Update progress
            progress = 50 + (i + 1) / len(papers) * 40
            search_status['progress'] = progress
        
        if not search_status['is_searching']:
            return
        
        # 完成搜索 / Complete search
        search_status.update({
            'is_searching': False,
            'progress': 100,
            'message': f'✅ 搜索完成！找到 {len(papers)} 篇相关论文 / Search completed! Found {len(papers)} relevant papers',
            'papers': papers
        })
        
    except Exception as e:
        search_status.update({
            'is_searching': False,
            'progress': 0,
            'message': f'❌ 搜索出错 / Search error: {str(e)}',
            'papers': []
        })

@app.route('/api/status')
def get_status():
    """获取搜索状态 / Get search status"""
    return jsonify(search_status)

@app.route('/api/stop')
def stop_search():
    """停止搜索 / Stop search"""
    global search_status
    search_status['is_searching'] = False
    search_status['message'] = '搜索已停止 / Search stopped'
    return jsonify({'message': '搜索已停止 / Search stopped'})

@app.route('/api/download/<format_type>')
def download_report(format_type):
    """下载报告 / Download report"""
    if not search_status['papers']:
        return jsonify({'error': '没有可下载的报告 / No report available for download'}), 400
    
    try:
        # 从请求参数获取关键词 / Get keywords from request parameters
        keywords_text = request.args.get('keywords', '')
        keywords = [k.strip() for k in keywords_text.split(',') if k.strip()]
        
        if format_type == 'html':
            content = reporter.generate_html_report(search_status['papers'], keywords)
            filename = f"arxiv_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            mimetype = 'text/html'
        else:
            content = reporter.generate_markdown_report(search_status['papers'], keywords)
            filename = f"arxiv_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            mimetype = 'text/markdown'
        
        # 创建临时文件 / Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix=f'.{format_type}', delete=False, encoding='utf-8') as f:
            f.write(content)
            temp_path = f.name
        
        return send_file(
            temp_path,
            as_attachment=True,
            download_name=filename,
            mimetype=mimetype
        )
        
    except Exception as e:
        return jsonify({'error': f'下载失败 / Download failed: {str(e)}'}), 500

if __name__ == '__main__':
    print("🌐 启动 arXiv 论文推送系统 双语Web版本... / Starting arXiv Paper Push System Bilingual Web Version...")
    print(f"📊 OpenAI API 状态 / OpenAI API Status: {'✅ 已配置 / Configured' if has_openai_api else '⚠️ 未配置 / Not configured'}")
    print("🌐 访问地址 / Access URL: http://localhost:52947")
    print("🔄 支持中英文界面切换 / Supports Chinese-English interface switching")
    print("按 Ctrl+C 停止服务器 / Press Ctrl+C to stop server")
    
    app.run(host='0.0.0.0', port=52948, debug=False)
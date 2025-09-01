#!/usr/bin/env python3
"""
arXiv 论文推送系统 - 启动脚本 / arXiv Paper Push System - Startup Script
让用户选择运行模式 / Let users choose running mode
"""

import sys
import os
import subprocess
import webbrowser
import time

def print_banner():
    """打印欢迎横幅 / Print welcome banner"""
    print("=" * 60)
    print("📚 arXiv Paper Push System / arXiv 论文推送系统")
    print("=" * 60)
    print("Intelligent academic paper tracking tool / 智能学术论文跟踪工具")
    print("Push latest papers based on keywords / 根据关键词推送最新论文")
    print()

def print_menu():
    """打印菜单选项 / Print menu options"""
    print("Please select running mode / 请选择运行模式:")
    print()
    print("1. 🌐 Web Interface Version (Recommended) / Web界面版本 (推荐)")
    print("   - Modern web interface, intuitive operation / 现代化Web界面，操作简单直观")
    print("   - Real-time progress display / 实时进度显示，支持中途停止")
    print("   - Online preview and download reports / 支持在线预览和下载报告")
    print("   - Access: http://localhost:59226 / 访问地址: http://localhost:59226")
    print()
    print("2. 💻 Command Line Demo Version / 命令行演示版本")
    print("   - Fast search, direct terminal display / 快速搜索，直接在终端显示结果")
    print("   - No API key required / 无需API密钥，使用论文摘要")
    print("   - Support HTML and Markdown reports / 支持保存HTML和Markdown报告")
    print()
    print("3. 🤖 Command Line Full Version / 命令行完整版本")
    print("   - Support OpenAI API for AI summaries / 支持OpenAI API生成AI总结")
    print("   - Support scheduled push / 支持定时推送功能")
    print("   - Requires API key configuration / 需要配置API密钥")
    print()
    print("4. ⚙️ Configure OpenAI API Key / 配置OpenAI API密钥")
    print("   - Set API key for AI summary feature / 设置API密钥以启用AI总结功能")
    print()
    print("5. 📖 View User Guide / 查看使用说明")
    print("   - Detailed usage guide and FAQ / 详细的使用指南和常见问题")
    print()
    print("6. 🌐 Switch Language / 切换语言")
    print("   - Switch between English and Chinese / 在中英文之间切换")
    print()
    print("0. 🚪 Exit / 退出")
    print()

def start_web_demo():
    """启动Web演示版本 / Start web demo version"""
    print("🚀 Starting Web Interface Version... / 正在启动Web界面版本...")
    print("📊 Feature: No API key required / 特色: 无需OpenAI API密钥")
    print("🌐 Access URL: http://localhost:59226 / 访问地址: http://localhost:59226")
    print("Press Ctrl+C to stop server / 按 Ctrl+C 停止服务器")
    print()
    
    try:
        # 启动Web服务器 / Start web server
        process = subprocess.Popen([sys.executable, 'web_demo.py'])
        
        # 等待服务器启动 / Wait for server to start
        time.sleep(3)
        
        # 尝试打开浏览器 / Try to open browser
        try:
            webbrowser.open('http://localhost:59226')
            print("✅ Browser opened automatically / 浏览器已自动打开")
        except:
            print("⚠️ Cannot open browser automatically / 无法自动打开浏览器")
            print("Please visit manually: http://localhost:59226 / 请手动访问: http://localhost:59226")
        
        print("\nServer is running... / 服务器正在运行中...")
        print("Press Ctrl+C to stop and return to menu / 按 Ctrl+C 停止服务器并返回主菜单")
        
        # 等待用户中断 / Wait for user interruption
        process.wait()
        
    except KeyboardInterrupt:
        print("\n⏹️ Stopping server... / 正在停止服务器...")
        process.terminate()
        process.wait()
        print("✅ Server stopped / 服务器已停止")
    except Exception as e:
        print(f"❌ Failed to start: {e} / 启动失败: {e}")

def start_cli_demo():
    """启动命令行演示版本 / Start command line demo version"""
    print("🚀 Starting Command Line Demo Version... / 正在启动命令行演示版本...")
    print()
    
    # 获取用户输入 / Get user input
    keywords = input("🔍 Enter search keywords (comma-separated) / 请输入搜索关键词 (多个关键词用逗号分隔): ").strip()
    if not keywords:
        keywords = "machine learning, deep learning"
        print(f"Using default keywords / 使用默认关键词: {keywords}")
    
    days = input("📅 Search recent days (default 7) / 搜索最近几天的论文 (默认7天): ").strip()
    if not days:
        days = "7"
    
    print()
    print("Starting search... / 开始搜索...")
    
    try:
        # 运行演示版本 / Run demo version
        cmd = [sys.executable, 'demo.py', '-k'] + keywords.split(',') + ['-d', days]
        subprocess.run(cmd)
    except Exception as e:
        print(f"❌ Execution failed / 运行失败: {e}")

def configure_api_key():
    """配置OpenAI API密钥 / Configure OpenAI API key"""
    print("⚙️ Configure OpenAI API Key / 配置OpenAI API密钥")
    print()
    print("How to get OpenAI API key / 如何获取OpenAI API密钥:")
    print("1. Visit https://platform.openai.com/ / 访问 https://platform.openai.com/")
    print("2. Register and login / 注册账号并登录")
    print("3. Create new key in API Keys page / 在API Keys页面创建新的密钥")
    print("4. Copy and enter the key below / 复制密钥并在下方输入")
    print()
    
    api_key = input("Enter your OpenAI API key (leave empty to cancel) / 请输入您的OpenAI API密钥 (留空取消): ").strip()
    
    if not api_key:
        print("❌ Configuration cancelled / 已取消配置")
        return
    
    try:
        # 更新.env文件 / Update .env file
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(f"OPENAI_API_KEY={api_key}\n")
        
        print("✅ API key configured successfully! / API密钥配置成功！")
        print("Now you can use full version with AI summaries / 现在可以使用完整版本获得AI总结功能")
        
    except Exception as e:
        print(f"❌ Configuration failed / 配置失败: {e}")

def show_help():
    """显示使用说明 / Show user guide"""
    print("📖 User Guide / 使用说明")
    print()
    
    help_text = """
🔍 Basic Usage / 基本使用:
1. Choose appropriate running mode / 选择合适的运行模式
2. Enter search keywords (English recommended) / 输入搜索关键词（建议使用英文）
3. Set search parameters (days, count, etc.) / 设置搜索参数（天数、数量等）
4. Wait for search completion and view results / 等待搜索完成并查看结果

💡 Keyword Suggestions / 关键词建议:
- English keywords work better / 使用英文关键词效果更好
- Use multiple keywords separated by commas / 可以使用多个关键词，用逗号分隔
- Common keywords: machine learning, deep learning, neural networks,
  computer vision, natural language processing, transformer, etc.
- 常用关键词: machine learning, deep learning, neural networks,
  computer vision, natural language processing, transformer 等

📊 Parameter Description / 参数说明:
- Search days: 3-7 days recommended / 搜索天数: 建议3-7天，平衡新颖性和数量
- Paper count: 10-20 papers recommended / 论文数量: 建议10-20篇，避免信息过载
- Summary language: Chinese or English / 总结语言: 中文或英文

🌐 Web Version Features / Web版本特色:
- Modern interface, easy operation / 现代化界面，操作简单
- Real-time progress display / 实时进度显示
- Online preview and download / 支持在线预览和下载
- No command line required / 无需命令行操作

💻 Command Line Features / 命令行版本特色:
- Fast execution / 运行速度快
- Batch processing support / 支持批量处理
- Scheduled push support / 支持定时推送
- Suitable for automation / 适合自动化场景

🤖 AI Summary Feature / AI总结功能:
- Requires OpenAI API key / 需要OpenAI API密钥
- Generate Chinese/English summaries / 生成中英文总结
- Extract paper key points / 提取论文要点
- Easy to understand quickly / 便于快速理解

📄 Output Formats / 输出格式:
- HTML: Beautiful web format, suitable for reading / HTML: 精美网页格式，适合阅读
- Markdown: Plain text format, easy to edit / Markdown: 纯文本格式，便于编辑

❓ FAQ / 常见问题:
Q: No papers found? / 搜索不到论文怎么办？
A: Try more general keywords or increase search days / 尝试使用更通用的关键词，或增加搜索天数

Q: Can I use without API key? / 没有API密钥可以使用吗？
A: Yes, demo version uses original abstracts / 可以，演示版本使用论文原始摘要，功能完全可用

Q: How to set up scheduled push? / 如何定时推送？
A: Use command line full version with time setting / 使用命令行完整版本，设置推送时间即可

Q: Support Chinese keywords? / 支持中文关键词吗？
A: Yes, but English keywords work better / 支持，但英文关键词搜索效果更好
"""
    
    print(help_text)
    input("\nPress Enter to return to menu / 按回车键返回主菜单...")

def main():
    """主函数 / Main function"""
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')  # 清屏 / Clear screen
        print_banner()
        print_menu()
        
        try:
            choice = input("Please select (0-6) / 请选择 (0-6): ").strip()
            
            if choice == '0':
                print("👋 Thank you for using arXiv Paper Push System! / 感谢使用 arXiv 论文推送系统！")
                break
            elif choice == '1':
                start_web_demo()
            elif choice == '2':
                start_cli_demo()
            elif choice == '3':
                start_cli_full()
            elif choice == '4':
                configure_api_key()
            elif choice == '5':
                show_help()
            elif choice == '6':
                switch_language()
            else:
                print("❌ Invalid choice, please try again / 无效选择，请重新输入")
                time.sleep(2)
                continue
                
        except KeyboardInterrupt:
            print("\n👋 Thank you for using arXiv Paper Push System! / 感谢使用 arXiv 论文推送系统！")
            break
        except Exception as e:
            print(f"❌ Error occurred / 发生错误: {e}")
            time.sleep(2)
        
        if choice != '0':
            input("\nPress Enter to return to menu / 按回车键返回主菜单...")

def start_cli_full():
    """启动命令行完整版本 / Start command line full version"""
    print("🚀 Starting Command Line Full Version... / 正在启动命令行完整版本...")
    print()
    
    # 检查API密钥 / Check API key
    try:
        from config import OPENAI_API_KEY
        if not OPENAI_API_KEY:
            print("⚠️ OpenAI API key not configured / 未配置OpenAI API密钥")
            print("Will use paper abstracts as summaries / 将使用论文摘要作为总结")
            print("To enable AI summaries, select option 4 / 如需AI总结功能，请选择菜单选项4配置API密钥")
            print()
    except:
        print("⚠️ Configuration file not found / 配置文件未找到")
    
    # 获取用户输入 / Get user input
    keywords = input("🔍 Enter search keywords (comma-separated) / 请输入搜索关键词 (多个关键词用逗号分隔): ").strip()
    if not keywords:
        keywords = "machine learning, deep learning"
        print(f"Using default keywords / 使用默认关键词: {keywords}")
    
    days = input("📅 Search recent days (default 7) / 搜索最近几天的论文 (默认7天): ").strip()
    if not days:
        days = "7"
    
    schedule_time = input("⏰ Scheduled push time (HH:MM format, leave empty for immediate run) / 定时推送时间 (格式HH:MM，留空表示立即运行): ").strip()
    
    print()
    print("Starting search... / 开始搜索...")
    
    try:
        # 构建命令 / Build command
        cmd = [sys.executable, 'main.py', '-k'] + keywords.split(',') + ['-d', days]
        if schedule_time:
            cmd.extend(['-s', schedule_time])
        
        subprocess.run(cmd)
    except Exception as e:
        print(f"❌ Execution failed / 运行失败: {e}")

def switch_language():
    """切换语言 / Switch language"""
    print("🌐 Language Switch / 语言切换")
    print()
    print("This feature will be available in future versions.")
    print("此功能将在未来版本中提供。")
    print()
    print("Current version supports bilingual interface.")
    print("当前版本支持双语界面。")
    time.sleep(3)

if __name__ == "__main__":
    main()

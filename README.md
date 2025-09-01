# 📚 arXiv Paper Push System

An intelligent academic paper tracking tool based on Python that automatically pushes the latest papers from arXiv based on your keywords (up to 10 papers daily) and generates brief summaries for each paper.

# 📚 arXiv 论文推送系统

一个基于Python的智能学术论文跟踪工具，可以根据你输入的关键词，每天自动推送arXiv上相关方向的新文章（最多10篇），并为每篇论文生成简短总结。

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![arXiv](https://img.shields.io/badge/arXiv-API-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)


## ✨ Features

- 🔍 **Smart Search**: Search for latest papers on arXiv based on keywords
- 📅 **Scheduled Push**: Support daily scheduled automatic push
- 🤖 **AI Summaries**: Use OpenAI API to generate Chinese/English summaries for each paper
- 📄 **Beautiful Reports**: Support HTML and Markdown format beautiful reports
- ⚙️ **Flexible Configuration**: Customizable search keywords, time range and other parameters
- 🎯 **Dual Version Support**: Provide full version and demo version for different needs


## ✨ 功能特性

- 🔍 **智能搜索**: 根据关键词搜索arXiv上的最新论文
- 📅 **定时推送**: 支持每日定时自动推送
- 🤖 **AI总结**: 使用OpenAI API为每篇论文生成中文总结
- 📄 **精美报告**: 支持HTML和Markdown格式的精美报告
- ⚙️ **灵活配置**: 可自定义搜索关键词、时间范围等参数
- 🎯 **双版本支持**: 提供完整版和演示版，适应不同需求

## 🚀 Quick Start

### Method 1: One-Click Launch (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run startup script, choose running mode
python3 start.py
```

### Method 2: Web Interface Version (Easiest)

```bash
# Start web interface (no API key required)
python3 web_demo.py

# Visit http://localhost:59226 in browser
```

### Method 3: Command Line Version

```bash
# Demo version (no API key required)
python3 demo.py -k "deep learning" -d 7

# Full version (supports AI summaries)
python3 main.py -k "machine learning" -d 7
```


## 🚀 快速开始

### 方法一：一键启动（推荐）

```bash
# 安装依赖
pip install -r requirements.txt

# 运行启动脚本，选择运行模式
python3 start.py
```

### 方法二：Web界面版本（最简单）

```bash
# 启动Web界面（无需API密钥）
python3 web_demo.py

# 在浏览器中访问 http://localhost:59226
```

### 方法三：命令行版本

```bash
# 演示版本（无需API密钥）
python3 demo.py -k "deep learning" -d 7

# 完整版本（支持AI总结）
python3 main.py -k "machine learning" -d 7
```

## 📖 Usage Examples

### Demo Version (Recommended for Beginners)

No API key required, uses paper abstracts as summaries:

```bash
# Search deep learning related papers
python3 demo.py -k "deep learning" -d 7

# Search multiple keywords
python3 demo.py -k "transformer" "attention" "neural network"

# Generate Markdown format report
python3 demo.py -k "computer vision" -f markdown

# Display in console only, don't save files
python3 demo.py -k "machine learning" --no-save
```

### Full Version (Requires OpenAI API)

Provides AI-generated Chinese/English summaries:

```bash
# Basic usage
python3 main.py -k "artificial intelligence" -d 5

# Scheduled push: automatically push at 9 AM daily
python3 main.py -k "machine learning" "AI" -s 09:00

# Scheduled push: push computer vision papers at 6 PM daily
python3 main.py -k "computer vision" "object detection" -s 18:00
```


## 📖 使用示例

### 演示版本（推荐新手）

无需API密钥，使用论文摘要作为总结：

```bash
# 搜索深度学习相关论文
python3 demo.py -k "deep learning" -d 7

# 搜索多个关键词
python3 demo.py -k "transformer" "attention" "neural network"

# 生成Markdown格式报告
python3 demo.py -k "computer vision" -f markdown

# 只在控制台显示，不保存文件
python3 demo.py -k "machine learning" --no-save
```

### 完整版本（需要OpenAI API）

提供AI生成的中文总结：

```bash
# 基本使用
python3 main.py -k "artificial intelligence" -d 5

# 定时推送：每天上午9点自动推送
python3 main.py -k "machine learning" "AI" -s 09:00

# 定时推送：每天下午6点推送计算机视觉论文
python3 main.py -k "computer vision" "object detection" -s 18:00
```

## 📊 Output Features

The program generates beautiful reports containing:

- 📚 **Paper Title**: Clear display of complete title
- 👥 **Author Information**: Smart display of main authors
- 📅 **Publication Date**: arXiv publication time
- 🏷️ **Paper Categories**: Subject classification tags
- 📝 **Smart Summary**: AI-generated Chinese/English summary or paper abstract
- 🔗 **Convenient Links**: Direct access to papers and PDF downloads

### HTML Report Example
- 🎨 Beautiful web format with responsive design
- 🌈 Clear color scheme and layout
- 📱 Support for mobile device viewing

### Markdown Report Example
- 📝 Plain text format, easy to edit and share
- 🔗 Support for GitHub and other platform rendering
- 📋 Easy to copy to other documents

## 📊 输出效果

程序会生成包含以下信息的精美报告：

- 📚 **论文标题**: 清晰显示完整标题
- 👥 **作者信息**: 智能显示主要作者
- 📅 **发布日期**: arXiv发布时间
- 🏷️ **论文分类**: 学科分类标签
- 📝 **智能总结**: AI生成的中文总结或论文摘要
- 🔗 **便捷链接**: 直接访问论文和PDF下载

### HTML报告示例
- 🎨 精美的网页格式，响应式设计
- 🌈 清晰的颜色搭配和排版
- 📱 支持移动设备查看

### Markdown报告示例
- 📝 纯文本格式，便于编辑和分享
- 🔗 支持GitHub等平台渲染
- 📋 便于复制到其他文档


## ⚙️ Configuration Options

| Parameter | Short | Description | Default |
|-----------|-------|-------------|---------|
| `--keywords` | `-k` | Search keywords (multiple allowed) | machine learning, deep learning, AI, neural networks |
| `--days` | `-d` | Search papers from recent days | 1 |
| `--format` | `-f` | Output format (html/markdown) | html |
| `--schedule` | `-s` | Scheduled push time (HH:MM) | None |
| `--no-save` | | Don't save files, display in console only | False |

### Custom Configuration

Edit `config.py` file:

```python
# Maximum number of results per search
MAX_RESULTS = 10

# Search papers from recent days
DAYS_BACK = 1

# Default search keywords
DEFAULT_KEYWORDS = [
    "machine learning",
    "deep learning", 
    "artificial intelligence",
    "neural networks"
]

# Summary language (chinese/english)
SUMMARY_LANGUAGE = "chinese"
```


## ⚙️ 配置选项

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--keywords` | `-k` | 搜索关键词（可多个） | machine learning, deep learning, AI, neural networks |
| `--days` | `-d` | 搜索最近几天的论文 | 1 |
| `--format` | `-f` | 输出格式（html/markdown） | html |
| `--schedule` | `-s` | 定时推送时间（HH:MM） | 无 |
| `--no-save` | | 不保存文件，只在控制台显示 | False |

### 自定义配置

编辑 `config.py` 文件：

```python
# 每次搜索的最大结果数
MAX_RESULTS = 10

# 搜索最近几天的论文
DAYS_BACK = 1

# 默认搜索关键词
DEFAULT_KEYWORDS = [
    "machine learning",
    "deep learning", 
    "artificial intelligence",
    "neural networks"
]

# 总结语言（chinese/english）
SUMMARY_LANGUAGE = "chinese"
```

## 📁 Project Structure

```
├── start.py            # 🚀 Startup script (recommended entry)
├── web_demo.py         # 🌐 Web interface version (demo)
├── web_app.py          # 🌐 Web interface version (full)
├── main.py             # 💻 Command line version (full)
├── demo.py             # 💻 Command line version (demo)
├── simple_gui.py       # 🖥️ Desktop GUI version (requires GUI)
├── gui_app.py          # 🖥️ Advanced GUI version (requires GUI)
├── arxiv_fetcher.py    # 📡 arXiv paper fetching module
├── summarizer.py       # 🤖 AI summary generation module
├── report_generator.py # 📄 Report generation module
├── config.py          # ⚙️ Configuration file
├── requirements.txt   # 📦 Dependencies list
├── install.sh         # 🔧 Auto installation script
├── .env.example      # 🔑 Environment variables template
├── User_Guide_EN.md   # 📚 Detailed user guide (English)
├── templates/        # 🎨 Web interface templates
└── reports/          # 📊 Report output directory
```


## 📁 项目结构

```
├── start.py            # 🚀 启动脚本（推荐入口）
├── web_demo.py         # 🌐 Web界面版本（演示版）
├── web_app.py          # 🌐 Web界面版本（完整版）
├── main.py             # 💻 命令行版本（完整版）
├── demo.py             # 💻 命令行版本（演示版）
├── simple_gui.py       # 🖥️ 桌面GUI版本（需要图形界面）
├── gui_app.py          # 🖥️ 高级GUI版本（需要图形界面）
├── arxiv_fetcher.py    # 📡 arXiv论文获取模块
├── summarizer.py       # 🤖 AI总结生成模块
├── report_generator.py # 📄 报告生成模块
├── config.py          # ⚙️ 配置文件
├── requirements.txt   # 📦 依赖包列表
├── install.sh         # 🔧 自动安装脚本
├── .env.example      # 🔑 环境变量模板
├── 使用说明.md        # 📚 详细使用说明
├── templates/        # 🎨 Web界面模板
└── reports/          # 📊 报告输出目录
```

## 🔧 FAQ

<details>
<summary><strong>Q: Why can't I find any papers?</strong></summary>

Possible reasons and solutions:
- Keywords too specific → Use more general keywords
- Time range too short → Increase search days (-d parameter)
- Using Chinese keywords → Try English keywords
</details>

<details>
<summary><strong>Q: What if I don't have an OpenAI API key?</strong></summary>

Use the demo version `demo.py`, which uses paper abstracts as summaries and is fully functional.
</details>

<details>
<summary><strong>Q: How to get an OpenAI API key?</strong></summary>

1. Visit [OpenAI Official Website](https://platform.openai.com/)
2. Register an account and log in
3. Create a new key in the API Keys page
4. Add the key to the `.env` file
</details>

<details>
<summary><strong>Q: Can I modify the number of papers searched?</strong></summary>

Yes, modify the `MAX_RESULTS` parameter in `config.py`.
</details>


## 🔧 常见问题

<details>
<summary><strong>Q: 为什么搜索不到论文？</strong></summary>

可能的原因和解决方案：
- 关键词太具体 → 使用更通用的关键词
- 时间范围太短 → 增加搜索天数（-d 参数）
- 使用中文关键词 → 尝试英文关键词
</details>

<details>
<summary><strong>Q: 没有OpenAI API密钥怎么办？</strong></summary>

使用演示版本 `demo.py`，它会使用论文摘要作为总结，功能完全可用。
</details>

<details>
<summary><strong>Q: 如何获取OpenAI API密钥？</strong></summary>

1. 访问 [OpenAI官网](https://platform.openai.com/)
2. 注册账号并登录
3. 在API Keys页面创建新的密钥
4. 将密钥添加到 `.env` 文件中
</details>

<details>
<summary><strong>Q: 可以修改搜索的论文数量吗？</strong></summary>

可以，修改 `config.py` 中的 `MAX_RESULTS` 参数。
</details>

## 🌟 Usage Tips

1. **Keyword Selection**: 
   - English keywords work better
   - Can combine multiple related keywords
   - Avoid overly specific terms

2. **Time Range**: 
   - Recommend searching 3-7 days of papers
   - Balance novelty and quantity

3. **Scheduled Push**: 
   - Set to push on weekday mornings
   - Convenient for timely understanding of latest research

4. **Report Format**: 
   - HTML format is more beautiful, suitable for reading
   - Markdown format is convenient for sharing and editing


## 🌟 使用建议

1. **关键词选择**: 
   - 使用英文关键词效果更好
   - 可以组合多个相关关键词
   - 避免过于具体的术语

2. **时间范围**: 
   - 建议搜索3-7天的论文
   - 平衡新颖性和数量

3. **定时推送**: 
   - 设置在工作日早上推送
   - 便于及时了解最新研究

4. **报告格式**: 
   - HTML格式更美观，适合阅读
   - Markdown格式便于分享和编辑

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！


## 📄 License

MIT License - See [LICENSE](LICENSE) file for details


## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件



## 🙏 Acknowledgments

- [arXiv](https://arxiv.org/) - Providing open academic paper database
- [OpenAI](https://openai.com/) - Providing powerful AI summarization capabilities
- All contributors and users for their support

---

⭐ If this project helps you, please give it a Star to support us!

## 🙏 致谢

- [arXiv](https://arxiv.org/) - 提供开放的学术论文数据库
- [OpenAI](https://openai.com/) - 提供强大的AI总结能力
- 所有贡献者和用户的支持

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！












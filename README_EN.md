# 📚 arXiv Paper Push System

An intelligent academic paper tracking tool based on Python that automatically pushes the latest papers from arXiv based on your keywords (up to 10 papers daily) and generates brief summaries for each paper.

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

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- [arXiv](https://arxiv.org/) - Providing open academic paper database
- [OpenAI](https://openai.com/) - Providing powerful AI summarization capabilities
- All contributors and users for their support

---

⭐ If this project helps you, please give it a Star to support us!
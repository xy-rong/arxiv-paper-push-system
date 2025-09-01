# 📚 arXiv Paper Push System - User Guide

## 🎯 System Overview

The arXiv Paper Push System is an intelligent academic paper tracking tool that helps researchers stay updated with the latest papers in their field of interest. The system automatically searches arXiv for relevant papers based on your keywords and generates comprehensive reports with summaries.

## 🚀 Getting Started

### System Requirements

- Python 3.7 or higher
- Internet connection for accessing arXiv API
- (Optional) OpenAI API key for AI-generated summaries

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd arxiv-paper-push-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment (optional)**
   ```bash
   cp .env.example .env
   # Edit .env file to add your OpenAI API key
   ```

## 🌐 Web Interface Version (Recommended)

### Starting the Web Interface

```bash
# Demo version (no API key required)
python3 web_demo.py

# Full version (with AI summaries)
python3 web_app.py
```

### Using the Web Interface

1. **Access the interface**: Open your browser and go to `http://localhost:59226`

2. **Configure search parameters**:
   - **Keywords**: Enter search terms separated by commas
   - **Search Days**: Choose how many recent days to search (1-14 days)
   - **Paper Count**: Select number of papers to retrieve (5-25 papers)
   - **Summary Language**: Choose Chinese or English for summaries
   - **Output Format**: Select HTML or Markdown for reports

3. **Start searching**: Click the "🚀 Start Search" button

4. **Monitor progress**: Watch the real-time progress bar and status messages

5. **View results**: Browse the search results displayed on the page

6. **Download or preview**: Use the download or preview buttons to save or view reports

### Web Interface Features

- **Real-time progress tracking**: See search progress and current status
- **Interactive controls**: Start, stop, download, and preview functions
- **Responsive design**: Works on desktop and mobile devices
- **No installation required**: Just open in any modern web browser

## 💻 Command Line Version

### Demo Version (No API Key Required)

```bash
# Basic usage
python3 demo.py -k "machine learning" -d 7

# Multiple keywords
python3 demo.py -k "deep learning,neural networks,transformer" -d 5

# Different output format
python3 demo.py -k "computer vision" -f markdown

# Display only (no file saving)
python3 demo.py -k "artificial intelligence" --no-save
```

### Full Version (With AI Summaries)

```bash
# Basic usage with AI summaries
python3 main.py -k "machine learning" -d 7

# Scheduled daily push at 9:00 AM
python3 main.py -k "deep learning" -s 09:00

# Multiple keywords with scheduling
python3 main.py -k "computer vision,object detection" -s 18:00
```

### Command Line Parameters

| Parameter | Short | Description | Example |
|-----------|-------|-------------|---------|
| `--keywords` | `-k` | Search keywords (comma-separated) | `-k "AI,ML,DL"` |
| `--days` | `-d` | Days to search back | `-d 7` |
| `--format` | `-f` | Output format (html/markdown) | `-f markdown` |
| `--schedule` | `-s` | Schedule time (HH:MM) | `-s 09:00` |
| `--no-save` | | Don't save files | `--no-save` |

## 🖥️ Desktop GUI Version

### Requirements

- Graphical desktop environment
- Display server (X11, Wayland, etc.)

### Starting the GUI

```bash
# Simple GUI version
python3 simple_gui.py

# Advanced GUI version (with modern themes)
python3 gui_app.py
```

### GUI Features

- **Native desktop application**: Integrated with your operating system
- **User-friendly interface**: Point-and-click operation
- **Real-time feedback**: Progress bars and status updates
- **File management**: Easy saving and opening of reports

## 🚀 One-Click Startup Script

### Using the Startup Script

```bash
python3 start.py
```

### Menu Options

1. **🌐 Web Interface Version (Recommended)**
   - Modern web interface with intuitive operation
   - Real-time progress display with stop support
   - Online preview and download reports
   - Access at: http://localhost:59226

2. **💻 Command Line Demo Version**
   - Fast search with direct terminal display
   - No API key required, uses paper abstracts
   - Supports HTML and Markdown report saving

3. **🤖 Command Line Full Version**
   - Supports OpenAI API for AI summaries
   - Supports scheduled push functionality
   - Requires API key configuration

4. **⚙️ Configure OpenAI API Key**
   - Set API key to enable AI summary functionality

5. **📖 View User Guide**
   - Detailed usage guide and FAQ

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI API Key (optional)
OPENAI_API_KEY=your_openai_api_key_here

# Default configuration (optional)
DEFAULT_KEYWORDS=machine learning,deep learning,AI
MAX_RESULTS=10
DAYS_BACK=1
SUMMARY_LANGUAGE=chinese
```

### Configuration File

Edit `config.py` to customize default settings:

```python
# Maximum number of results per search
MAX_RESULTS = 10

# Default search keywords
DEFAULT_KEYWORDS = [
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "neural networks"
]

# Default number of days to search back
DAYS_BACK = 1

# Summary language (chinese/english)
SUMMARY_LANGUAGE = "chinese"

# Report output directory
REPORTS_DIR = "reports"
```

## 📊 Understanding the Output

### Report Structure

Each generated report contains:

1. **Header Information**
   - Report generation date and time
   - Search keywords used
   - Number of papers found

2. **Paper Entries**
   - Paper title and authors
   - Publication date and categories
   - Abstract or AI-generated summary
   - Links to paper and PDF

3. **Footer Information**
   - Generation timestamp
   - System information

### Output Formats

#### HTML Format
- **Advantages**: Beautiful formatting, easy to read, responsive design
- **Use cases**: Reading, sharing, web publishing
- **Features**: Clickable links, styled layout, mobile-friendly

#### Markdown Format
- **Advantages**: Plain text, easy to edit, version control friendly
- **Use cases**: Documentation, GitHub, technical writing
- **Features**: Simple syntax, portable, widely supported

## 🔍 Search Strategies

### Keyword Selection

1. **Use English keywords**: Better search results on arXiv
2. **Be specific but not too narrow**: Balance relevance and quantity
3. **Use multiple related terms**: Increase coverage
4. **Avoid overly technical jargon**: Unless specifically needed

### Examples of Good Keywords

- **Machine Learning**: "machine learning", "ML", "supervised learning"
- **Deep Learning**: "deep learning", "neural networks", "CNN", "RNN"
- **Computer Vision**: "computer vision", "image processing", "object detection"
- **Natural Language Processing**: "NLP", "natural language processing", "text mining"

### Time Range Selection

- **1-3 days**: For very recent papers, daily updates
- **5-7 days**: Balanced approach, weekly summaries
- **10-14 days**: Comprehensive coverage, bi-weekly reviews

## 🤖 AI Summary Features

### OpenAI Integration

The system uses OpenAI's GPT-3.5 model to generate intelligent summaries:

1. **Automatic summarization**: Extracts key points from paper abstracts
2. **Language support**: Generates summaries in Chinese or English
3. **Contextual understanding**: Provides relevant and coherent summaries
4. **Customizable length**: Adjustable summary length and detail level

### Without API Key

If no OpenAI API key is configured:

1. **Uses original abstracts**: Shows the paper's original abstract
2. **Text cleaning**: Removes formatting and special characters
3. **Length optimization**: Truncates long abstracts for readability
4. **Full functionality**: All other features remain available

## 📅 Scheduling and Automation

### Setting Up Scheduled Pushes

```bash
# Daily push at 9:00 AM
python3 main.py -k "your keywords" -s 09:00

# The system will:
# 1. Wait until the specified time
# 2. Perform the search automatically
# 3. Generate and save reports
# 4. Continue running for the next day
```

### Automation Tips

1. **Use cron jobs** (Linux/macOS):
   ```bash
   # Add to crontab for daily execution at 9 AM
   0 9 * * * cd /path/to/project && python3 main.py -k "your keywords"
   ```

2. **Use Task Scheduler** (Windows):
   - Create a new task in Windows Task Scheduler
   - Set trigger for daily execution
   - Set action to run the Python script

3. **Use systemd** (Linux):
   - Create a systemd service and timer
   - Enable automatic startup and scheduling

## 🛠️ Troubleshooting

### Common Issues

1. **No papers found**
   - Check keyword spelling and relevance
   - Increase the search time range
   - Try more general keywords
   - Verify internet connection

2. **API key errors**
   - Verify the API key is correct
   - Check API key permissions and quotas
   - Ensure the `.env` file is properly formatted

3. **Installation issues**
   - Update pip: `pip install --upgrade pip`
   - Use virtual environment: `python -m venv venv`
   - Check Python version: `python --version`

4. **Web interface not accessible**
   - Check if the port is already in use
   - Try a different port number
   - Verify firewall settings

### Performance Optimization

1. **Reduce paper count**: Lower the `MAX_RESULTS` setting
2. **Optimize keywords**: Use more specific terms
3. **Limit time range**: Search fewer days
4. **Use demo version**: Skip AI processing for faster results

## 📈 Best Practices

### For Researchers

1. **Create keyword profiles**: Different sets for different research areas
2. **Regular scheduling**: Set up daily or weekly automated searches
3. **Organize reports**: Create folders for different topics
4. **Share findings**: Use Markdown format for collaboration

### For Institutions

1. **Centralized deployment**: Set up on a server for team access
2. **Custom configurations**: Tailor keywords for department needs
3. **Automated distribution**: Email reports to team members
4. **Archive management**: Organize historical reports

### For Developers

1. **API integration**: Incorporate into existing research tools
2. **Custom modifications**: Extend functionality for specific needs
3. **Data processing**: Use output for further analysis
4. **Workflow automation**: Integrate with other research workflows

## 🔮 Advanced Usage

### Custom Report Templates

You can modify the report templates in the `templates/` directory:

1. **HTML templates**: Edit CSS and HTML structure
2. **Markdown templates**: Customize formatting and layout
3. **Add new formats**: Create additional output formats

### API Integration

The system can be integrated into other applications:

```python
from arxiv_fetcher import ArxivFetcher
from summarizer import PaperSummarizer
from report_generator import ReportGenerator

# Initialize components
fetcher = ArxivFetcher(max_results=10)
summarizer = PaperSummarizer()
reporter = ReportGenerator()

# Search and process papers
papers = fetcher.search_papers(["machine learning"], days=7)
for paper in papers:
    paper['summary'] = summarizer.summarize_paper(paper)

# Generate report
report_path = reporter.save_report(papers, ["machine learning"], "html")
```

### Extending Functionality

1. **Add new data sources**: Integrate other academic databases
2. **Custom AI models**: Use different language models
3. **Enhanced filtering**: Add more sophisticated paper filtering
4. **Visualization**: Create charts and graphs from paper data

## 📞 Support and Community

### Getting Help

1. **Documentation**: Check this user guide and README files
2. **Issues**: Report bugs and request features on GitHub
3. **Discussions**: Join community discussions
4. **Examples**: Check the examples in the repository

### Contributing

1. **Bug reports**: Help improve the system by reporting issues
2. **Feature requests**: Suggest new functionality
3. **Code contributions**: Submit pull requests
4. **Documentation**: Help improve guides and examples

---

This user guide covers all aspects of using the arXiv Paper Push System. For the most up-to-date information, please check the project repository and documentation.
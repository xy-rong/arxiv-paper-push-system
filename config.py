import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API配置
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# arXiv搜索配置
MAX_RESULTS = 10  # 每次搜索的最大结果数
DAYS_BACK = 1     # 搜索最近几天的论文

# 默认搜索关键词（可以通过命令行参数覆盖）
DEFAULT_KEYWORDS = [
    "machine learning",
    "deep learning", 
    "artificial intelligence",
    "neural networks"
]

# 总结配置
SUMMARY_MAX_LENGTH = 200  # 总结的最大字符数
SUMMARY_LANGUAGE = "chinese"  # 总结语言：chinese 或 english
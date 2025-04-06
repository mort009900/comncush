import os

TOKEN = os.getenv ("7784061554:AAElO8fFvwPnJ9MPHXznfu2Qf8sokSjyqiQ")  # تأكد من صحة التوكن
DB_PATH = os.getenv("data/database.db")
BOOKS_FOLDER = "data/books/"
PAGES_FOLDER = "data/pages/"
PROXY_URL = os.getenv(None)
PAGES_SUBFOLDERS = [os.path.join(PAGES_FOLDER, f"FOLDER{i}") for i in range(1, 11)]

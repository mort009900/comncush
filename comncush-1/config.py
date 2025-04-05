import os

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace with your actual Telegram bot token
DB_PATH = "data/database.db"
BOOKS_FOLDER = "data/books/"
PAGES_FOLDER = "data/pages/"
PROXY_URL = None  # Set to your proxy URL if needed

PAGES_SUBFOLDERS = [os.path.join(PAGES_FOLDER, f"FOLDER{i}") for i in range(1, 11)]
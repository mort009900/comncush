import os

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # تأكد من صحة التوكن
DB_PATH = "data/database.db"
BOOKS_FOLDER = "data/books/"
PAGES_FOLDER = "data/pages/"
PROXY_URL = None  # إذا كنت تحتاج إلى بروكسي، ضع الرابط هنا

PAGES_SUBFOLDERS = [os.path.join(PAGES_FOLDER, f"FOLDER{i}") for i in range(1, 11)]
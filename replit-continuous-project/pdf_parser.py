import os
import sqlite3
import fitz  # PyMuPDF
from utils.text_to_image import extract_text_from_image

DB_PATH = "data/database.db"
BOOKS_FOLDER = "data/books/"
PAGES_FOLDER = "data/pages/"

def initialize_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)  # Ensure the data directory exists
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_content (
            page_number INTEGER,
            content TEXT,
            image_path TEXT,
            book_name TEXT,
            PRIMARY KEY (page_number, book_name)
        )
    """)
    conn.commit()
    conn.close()

def process_books():
    initialize_database()
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for book in os.listdir(BOOKS_FOLDER):
        if book.endswith(".pdf"):
            book_path = os.path.join(BOOKS_FOLDER, book)
            book_name = os.path.splitext(book)[0]
            doc = fitz.open(book_path)

            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text("text")
                image_path = os.path.join(PAGES_FOLDER, f"{book_name}_page_{page_num+1}.jpg")

                pix = page.get_pixmap()
                pix.save(image_path)

                if not text.strip():
                    text = extract_text_from_image(image_path)

                cursor.execute("INSERT OR REPLACE INTO book_content VALUES (?, ?, ?, ?)", 
                               (page_num + 1, text, image_path, book_name))

            doc.close()
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    process_books()
    print("✅ تم استخراج جميع الكتب وتخزينها بنجاح!")
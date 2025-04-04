import os
import sqlite3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ApplicationBuilder
from fuzzywuzzy import fuzz
from utils.text_to_image import extract_text_from_image
from config import TOKEN, DB_PATH, PROXY_URL  # استيراد الإعدادات

async def start(update: Update, context):
    await update.message.reply_text("👋 أرسل سؤالك كنص أو صورة     !")

def search_answer(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT page_number, content, image_path, book_name FROM book_content")
    results = cursor.fetchall()
    conn.close()

    best_match = None
    best_score = 0

    for page_number, content, image_path, book_name in results:
        score = fuzz.partial_ratio(query.lower(), content.lower())
        if score > best_score:
            best_score = score
            best_match = (page_number, content, image_path, book_name)

    return best_match if best_score > 50 else None

async def handle_text(update: Update, context):
    query = update.message.text
    result = search_answer(query)
    
    if result:
        page_number, _, image_path, book_name = result
        try:
            with open(image_path, "rb") as photo:
                keyboard = [[InlineKeyboardButton("⬅️ السابق", callback_data=f"prev_{page_number}_{book_name}"),
                             InlineKeyboardButton("التالي ➡️", callback_data=f"next_{page_number}_{book_name}")]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_photo(photo=photo, caption=f"📖 المصدر: {book_name}", reply_markup=reply_markup)
        except FileNotFoundError:
            await update.message.reply_text("❌ تعذر العثور على الصورة المطلوبة!")
    else:
        await update.message.reply_text("❌ لم أجد إجابة لسؤالك!")

async def handle_photo(update: Update, context):
    file = await update.message.photo[-1].get_file()
    file_path = "data/temp.jpg"
    await file.download_to_drive(file_path)

    query = extract_text_from_image(file_path)
    result = search_answer(query)
    
    if result:
        page_number, _, image_path, book_name = result
        try:
            with open(image_path, "rb") as photo:
                keyboard = [[InlineKeyboardButton("⬅️ السابق", callback_data=f"prev_{page_number}_{book_name}"),
                             InlineKeyboardButton("التالي ➡️", callback_data=f"next_{page_number}_{book_name}")]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_photo(photo=photo, caption=f"📖 المصدر: {book_name}", reply_markup=reply_markup)
        except FileNotFoundError:
            await update.message.reply_text("❌ تعذر العثور على الصورة المطلوبة!")
    else:
        await update.message.reply_text("❌ لم أجد إجابة لسؤالك!")

async def navigate_pages(update: Update, context):
    query = update.callback_query
    await query.answer()

    try:
        # تأكد من أن البيانات تحتوي على القيم الصحيحة
        action, page_number, book_name = query.data.split("_", maxsplit=2)  # استخدام maxsplit لتجنب الأخطاء
        page_number = int(page_number)

        # تحديد الصفحة الجديدة بناءً على الإجراء
        new_page = page_number + 1 if action == "next" else page_number - 1

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT image_path FROM book_content WHERE page_number = ? AND book_name = ?", (new_page, book_name))
        result = cursor.fetchone()
        conn.close()

        if result:
            image_path = result[0]
            try:
                with open(image_path, "rb") as photo:
                    keyboard = [[InlineKeyboardButton("⬅️ السابق", callback_data=f"prev_{new_page}_{book_name}"),
                                 InlineKeyboardButton("التالي ➡️", callback_data=f"next_{new_page}_{book_name}")]]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    await query.message.edit_media(media=InputMediaPhoto(photo), reply_markup=reply_markup)
            except FileNotFoundError:
                await query.message.reply_text("❌ تعذر العثور على الصورة المطلوبة!")
        else:
            await query.message.reply_text("❌ لا يوجد المزيد من الصفحات.")
    except ValueError:
        # معالجة الخطأ إذا كانت البيانات غير صحيحة
        await query.message.reply_text("❌ حدث خطأ في معالجة الطلب. الرجاء المحاولة مرة أخرى.")

def main():
    app = ApplicationBuilder().token(TOKEN).proxy_url(PROXY_URL).build() if PROXY_URL else ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CallbackQueryHandler(navigate_pages))

    app.run_polling(timeout=120, read_timeout=120)  # زيادة المهلة الزمنية

if __name__ == "__main__":
    main()

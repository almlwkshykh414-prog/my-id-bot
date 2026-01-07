import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# التوكن الخاص بك
TOKEN = '8106813714:AAGjqAvAM1rno9RgeiHkkHcY4KZzLXVDRF8'

async def send_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"الأيدي الخاص بك هو: {user_id}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.TEXT | filters.COMMAND, send_id)
    application.add_handler(handler)
    print("البوت يعمل الآن...")
    application.run_polling()

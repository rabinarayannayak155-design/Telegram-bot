from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("8543515466:AAHywcVzST7Hx3gAhoOea4fVPKDPCs3rA9Q")

YOUTUBE_LINK = "https://youtube.com/@ff_leaks_4_you?si=OCv14M5zRrqJbSJd"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send hi 👋")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "hi":
        await update.message.reply_text(
            f"Hi 👋\nSubscribe here 🔥\n👉 {YOUTUBE_LINK}"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot running...")
app.run_polling()

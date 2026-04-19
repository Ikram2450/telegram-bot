import sqlite3
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8202205111:AAEBuUiMyv-Ap4Fv9mhJhyQltSDhHCl3TEA")

# database create
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER
)
""")
conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # save user
    cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()

    text = """🎉 Welcome to Robot!

Please send your phone number starting with the country code.
(Example: +880xxxxxxxxxxx)

/cap send to check capacity"""

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()

from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this with your actual bot token
TOKEN = "7971054906:AAGN-e4cdbPZOI0OnGuFpQx33RrKZ2fBxO8"

# Flask app
app = Flask(__name__)

# Initialize Telegram bot
application = ApplicationBuilder().token(TOKEN).build()

# Command handler for "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Chill Goose Bot! 🪙")

application.add_handler(CommandHandler("start", start))

# Webhook route
@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    json_update = request.get_json(force=True)
    update = Update.de_json(json_update, application.bot)
    application.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

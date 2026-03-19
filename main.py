#!/usr/bin/env python3
"""
Simple Telegram bot (python-telegram-bot v20+)
Replies to /start and /help commands.
"""

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Token (Environment variable or default fallback)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8596938580:AAFze_XPVxlFTbU8YeBDmKkW74Pz21W8h8Y")

# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name if user else "there"
    await update.message.reply_text(
        f"👋 Hello {name}!\n\n"
        "This is a test /start bot.\n\n"
        "If you see this, the bot is running ✅"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Hello message\n/help - Show help")

# --- Main ---
def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN missing. Set environment variable BOT_TOKEN.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    logger.info("Bot started ✅")
    app.run_polling()

if __name__ == "__main__":
    main()

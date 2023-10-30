from core.mapper import Mapper
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging
import re


EMAIL_REQUEST_PATTERN = r"ایمیل|email"
TOKEN_FILE = "token"
f = open(TOKEN_FILE)
token = f.read().strip()
f.close()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there fellow student.\nAdd me to your groups and I shall provide the email of any professor from the CE department when a message containing their name and the word 'email' is sent.\nI am the work of Parsa and Kasra.")


async def handle_new_message(update, context):
    message = update.message.text.lower()
    if re.findall(EMAIL_REQUEST_PATTERN, message):
        mess = Mapper.get(message)
        if mess:
            await update.message.reply_text(mess)


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_new_message))
    
    application.run_polling()



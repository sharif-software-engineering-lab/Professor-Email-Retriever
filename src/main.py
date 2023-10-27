from core.mapper import Mapper
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging

TOKEN_FILE = "token"
f = open(TOKEN_FILE)
token = f.read().strip()
f.close()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def handle_new_message(update, context):
    message = update.message.text
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    # ... do something with the message, chat_id, user_id, etc.
    print(f"Received message in chat {chat_id} from user {user_id}: {message}")
    mess = Mapper.get(message)
    if mess:
        await update.message.reply_text(mess)


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_new_message))
    
    application.run_polling()



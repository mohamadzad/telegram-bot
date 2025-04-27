from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# توکن ربات خودت رو قرار بده
TOKEN = 'توکن خودت اینجا'

# تعریف مراحل برای ConversationHandler
NAME, EMAIL = range(2)

# chat_id خودت رو اینجا قرار بده
YOUR_CHAT_ID = 'چت آی دی خودت اینجا'

# تابع شروع تعامل
async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("سلام! لطفاً نام خود را وارد کنید.")
    return NAME

async def get_name(update: Update, context: CallbackContext) -> int:
    user_name = update.message.text
    context.user_data['name'] = user_name
    await update.message.reply_text("حالا لطفاً ایمیل خود را وارد کنید.")
    return EMAIL

async def get_email(update: Update, context: CallbackContext) -> int:
    user_email = update.message.text
    user_name = context.user_data['name']
    
    await context.bot.send_message(
        chat_id=YOUR_CHAT_ID,
        text=f"نام: {user_name}\nایمیل: {user_email}"
    )
    
    await update.message.reply_text("اطلاعات شما ارسال شد. با تشکر!")
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("تعامل لغو شد.")
    return ConversationHandler.END

def main():
    application = Application.builder().token(TOKEN).build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conversation_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
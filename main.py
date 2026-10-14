from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
##########

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    keyboard = [
        ["راهنما", "درباره ربات"]
    ]

    markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "سلام! از دکمه‌های زیر استفاده کن 🤖",
        reply_markup=markup
    )

##########

async def help_button(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await help_command(update, context)

###

async def about_button(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    
    description = description = await get_bot_description(context)

    if not description:
        description = "توضیحات ربات هنوز ثبت نشده است."

    await update.message.reply_text(description)
    
##########

async def get_bot_description(
    context: ContextTypes.DEFAULT_TYPE
) -> str:
    bot_info = await context.bot.get_my_description()
    description = bot_info.description.strip()

    if not description:
        description = "توضیحات ربات هنوز ثبت نشده است."

    return description
    
##########

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    description = await get_bot_description(context)

    if not description:
        description = "توضیحات ربات هنوز ثبت نشده است."

    help_text = (
        f"{description}\n\n"
        "دستورهای ربات:\n"
        "/start - شروع کار\n"
        "/help - راهنما\n\n"
        "همچنین می‌توانی یک پیام متنی بفرستی."
    )

    await update.message.reply_text(help_text)

##########

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(text)

##########

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
    MessageHandler(filters.Regex("^راهنما$"), help_button)
)

    app.add_handler(
    MessageHandler(filters.Regex("^درباره ربات$"), about_button)
)
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("ربات روشن شد!")
    app.run_polling()

##########

if __name__ == "__main__":
    main()
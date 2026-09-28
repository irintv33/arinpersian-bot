import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from openai import AsyncOpenAI

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\n"
        "به ربات هوشمند آرین پرشین خوش آمدید.\n"
        "سؤالتان را بپرسید تا پاسخ بدهم."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    try:
        response = await client.responses.create(
            model="gpt-4.1-mini",
            input=update.message.text,
        )

        answer = response.output_text
        await update.message.reply_text(answer[:4000])

    except Exception:
        await update.message.reply_text(
            "متأسفانه مشکلی پیش آمد. لطفاً دوباره تلاش کنید."
        )


def main():
    if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
        raise RuntimeError("توکن‌های ربات تنظیم نشده‌اند.")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    app.run_polling()


if __name__ == "__main__":
    main()

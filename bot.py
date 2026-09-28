import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

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


# -----------------------------
# HTTP Server برای Render
# -----------------------------

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Arin Persian Bot is running!")

    def log_message(self, format, *args):
        return


def run_web_server():
    port = int(os.getenv("PORT", "10000"))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


# -----------------------------
# Telegram Bot
# -----------------------------

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

    except Exception as e:
        print("OpenAI Error:", e)

        await update.message.reply_text(
            "www.irinpersian.ir متأسفانه مشکلی پیش آمد. لطفاً دوباره تلاش کنید."
        )


def main():
    if not TELEGRAM_TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN تنظیم نشده است.")

    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY تنظیم نشده است.")

    # اجرای وب‌سرور برای Render
    threading.Thread(
        target=run_web_server,
        daemon=True
    ).start()

    # اجرای ربات تلگرام
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat
        )
    )

    print("Arin Persian Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()

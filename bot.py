```python
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


# =========================
# Render Health Check
# =========================

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header(
            "Content-type",
            "text/plain; charset=utf-8"
        )
        self.end_headers()
        self.wfile.write(
            b"Arin Persian Secretary Bot is running!"
        )

    def log_message(self, format, *args):
        return


def run_web_server():
    port = int(os.getenv("PORT", "10000"))
    server = HTTPServer(
        ("0.0.0.0", port),
        HealthHandler
    )
    server.serve_forever()


# =========================
# Main Menu
# =========================

def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🛍 خدمات و محصولات",
                callback_data="services"
            )
        ],
        [
            InlineKeyboardButton(
                "⭐ Telegram Stars",
                callback_data="stars"
            ),
            InlineKeyboardButton(
                "💎 Telegram Premium",
                callback_data="premium"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 شماره مجازی",
                callback_data="numbers"
            ),
            InlineKeyboardButton(
                "📈 خدمات اینستاگرام",
                callback_data="instagram"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 خدمات تلگرام",
                callback_data="telegram"
            ),
            InlineKeyboardButton(
                "🖥 VPS",
                callback_data="vps"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 طراحی سایت",
                callback_data="website"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 راهنمای پرداخت",
                callback_data="payment"
            ),
            InlineKeyboardButton(
                "📦 پیگیری سفارش",
                callback_data="order"
```

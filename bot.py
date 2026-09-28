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
            )
        ],
        [
            InlineKeyboardButton(
                "🎫 پشتیبانی",
                callback_data="support"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 ورود به سایت",
                url="https://www.irinpersian.ir"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# Start
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        "👋 سلام و خوش آمدید به آرین پرشین\n\n"
        "🤖 منشی خودکار مجموعه در خدمت شماست.\n\n"
        "از منوی زیر می‌توانید خدمات موردنظر "
        "خود را انتخاب کنید:",
        reply_markup=main_menu()
    )


# =========================
# Button Handler
# =========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if not query:
        return

    await query.answer()
    data = query.data

    if data == "services":
        text = (
            "🛍 خدمات و محصولات آرین پرشین\n\n"
            "⭐ Telegram Stars\n"
            "💎 Telegram Premium\n"
            "📱 شماره مجازی\n"
            "📈 خدمات اینستاگرام\n"
            "📢 خدمات تلگرام\n"
            "🖥 VPS و سرور مجازی\n"
            "🌐 طراحی سایت\n"
            "🛒 محصولات آرایشی و بهداشتی\n\n"
            "برای مشاهده جزئیات و سفارش:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "stars":
        text = (
            "⭐ خرید Telegram Stars\n\n"
            "🔹 تحویل سریع\n"
            "🔹 پرداخت امن\n"
            "🔹 پشتیبانی\n\n"
            "برای مشاهده قیمت و ثبت سفارش:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "premium":
        text = (
            "💎 Telegram Premium\n\n"
            "اشتراک Telegram Premium "
            "در مدت‌های مختلف ارائه می‌شود.\n\n"
            "برای مشاهده قیمت و خرید:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "numbers":
        text = (
            "📱 شماره مجازی\n\n"
            "شماره مجازی برای سرویس‌های مختلف "
            "ارائه می‌شود.\n\n"
            "کشورها و سرویس‌های موجود را "
            "در سایت مشاهده کنید:\n\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "instagram":
        text = (
            "📈 خدمات اینستاگرام\n\n"
            "🔹 خدمات رشد پیج\n"
            "🔹 افزایش فالوور\n"
            "🔹 خدمات تعاملی\n\n"
            "جزئیات و سفارش:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "telegram":
        text = (
            "📢 خدمات تلگرام\n\n"
            "🔹 ممبر کانال و گروه\n"
            "🔹 ویو پست\n"
            "🔹 ریکشن\n"
            "🔹 ربات تلگرام\n"
            "🔹 Telegram Stars\n"
            "🔹 Telegram Premium\n\n"
            "مشاهده خدمات:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "vps":
        text = (
            "🖥 VPS و سرور مجازی\n\n"
            "ارائه سرورهای مجازی ایران و اروپا.\n\n"
            "برای مشاهده مشخصات و قیمت‌ها:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "website":
        text = (
            "🌐 طراحی سایت\n\n"
            "طراحی سایت فروشگاهی، خدماتی و اختصاصی.\n\n"
            "برای ثبت سفارش و دریافت اطلاعات:\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "payment":
        text = (
            "💳 راهنمای پرداخت\n\n"
            "1️⃣ محصول یا خدمت موردنظر را انتخاب کنید.\n"
            "2️⃣ وارد صفحه سفارش شوید.\n"
            "3️⃣ پرداخت را از طریق درگاه سایت انجام دهید.\n"
            "4️⃣ در صورت درخواست، اطلاعات سفارش را "
            "برای پشتیبانی ارسال کنید.\n\n"
            "⚠️ هنگام پرداخت، VPN را خاموش کنید.\n\n"
            "🌐 www.irinpersian.ir"
        )

    elif data == "order":
        text = (
            "📦 پیگیری سفارش\n\n"
            "برای پیگیری سفارش، شماره سفارش یا "
            "اطلاعات مربوط به خرید خود را برای "
            "پشتیبانی ارسال کنید.\n\n"
            "👨‍💻 پشتیبانی:\n"
            "@Technician404"
        )

    elif data == "support":
        text = (
            "🎫 پشتیبانی آرین پرشین\n\n"
            "اگر سؤال یا مشکلی دارید، از طریق "
            "آیدی زیر با پشتیبانی ارتباط بگیرید:\n\n"
            "👨‍💻 @Technician404\n\n"
            "🌐 www.irinpersian.ir"
        )

    else:
        text = "❌ گزینه نامعتبر است."

    back_button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 بازگشت به منوی اصلی",
                    callback_data="back"
                )
            ]
        ]
    )

    await query.edit_message_text(
        text,
        reply_markup=back_button
    )


# =========================
# Back To Main Menu
# =========================

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if not query:
        return

    await query.answer()

    await query.edit_message_text(
        "🤖 منوی اصلی آرین پرشین\n\n"
        "لطفاً گزینه موردنظر را انتخاب کنید:",
        reply_markup=main_menu()
    )


# =========================
# Normal Text Messages
# =========================

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    message = update.message.text.lower()

    if any(
        word in message
        for word in ["سلام", "درود", "hello", "hi"]
    ):
        await update.message.reply_text(
            "👋 سلام و خوش آمدید به آرین پرشین!\n\n"
            "🤖 منشی خودکار آماده پاسخگویی است.\n\n"
            "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
            reply_markup=main_menu()
        )
        return

    if any(
        word in message
        for word in ["پشتیبانی", "مشکل", "کمک", "ساپورت"]
    ):
        await update.message.reply_text(
            "🎫 پشتیبانی آرین پرشین\n\n"
            "👨‍💻 @Technician404\n\n"
            "🌐 www.irinpersian.ir"
        )
        return

    if any(
        word in message
        for word in ["قیمت", "خرید", "محصول", "هزینه"]
    ):
        await update.message.reply_text(
            "🛍 برای مشاهده قیمت‌ها و محصولات "
            "به سایت آرین پرشین مراجعه کنید:\n\n"
            "🌐 www.irinpersian.ir",
            reply_markup=main_menu()
        )
        return

    await update.message.reply_text(
        "🤖 پیام شما دریافت شد.\n\n"
        "برای مشاهده خدمات و دریافت راهنمایی، "
        "از منوی زیر استفاده کنید:",
        reply_markup=main_menu()
    )


# =========================
# Main
# =========================

def main():
    if not TELEGRAM_TOKEN:
        raise RuntimeError(
            "TELEGRAM_TOKEN تنظیم نشده است."
        )

    threading.Thread(
        target=run_web_server,
        daemon=True
    ).start()

    app = (
        Application
        .builder()
        .token(TELEGRAM_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(
            back,
            pattern="^back$"
        )
    )

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            text_message
        )
    )

    print(
        "Arin Persian Secretary Bot is running..."
    )

    app.run_polling()


if __name__ == "__main__":
    main()

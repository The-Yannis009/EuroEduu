from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8511865702:AAEBjyVjHRcmP6t485_tf1sJs7owmxxIIVU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Open App",
                web_app=WebAppInfo(url="https://prof-bot.base44.app")
            )
        ]
    ]

    await update.message.reply_text(
        "Click below to open the app 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ADMIN TELEGRAM ID (o'zingizniki, uni bot orqali topamiz pastroqda)
ADMIN_CHAT_ID = 634444923  # <-- buni o'zingiznikiga almashtiring

# /start buyrug'iga javob
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum!\nIltimos, murojaatingizni matn shaklida yuboring."
    )

# Murojaatni qabul qilish va adminga yuborish
async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    message = update.message.text
    user_info = f"👤 @{user.username if user.username else user.full_name} (ID: {user.id})"

    # Adminga yuboriladi
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"📩 Yangi murojaat:\n{user_info}\n\n✉️ {message}"
    )

    # Foydalanuvchiga tasdiq
    await update.message.reply_text("Murojaatingiz qabul qilindi. Rahmat!")

# Asosiy funksiyani ishga tushurish
if __name__ == '__main__':
    import os

    BOT_TOKEN = "7390734577:AAH1n5xvtTF4WeFykqwvV3xB4NGVhoObilU"  # <-- bu yerga BotFather bergan tokenni yozing

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), receive_message))

    print("Bot ishga tushdi...")
    app.run_polling()

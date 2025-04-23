import telebot
import os
from predict_model import predict_signal

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi. Railway Environment Variables’ni tekshiring.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Aviator signal bot ishga tushdi.")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    try:
        result, last_coeffs = predict_signal()
        coeffs_text = ", ".join([str(c) for c in last_coeffs])
        bot.send_message(
            message.chat.id,
            f"✈️ TEST SIGNAL - Aviator\n"
            f"Oxirgi 3 koeffitsiyent: [{coeffs_text}]\n"
            f"Ehtrimol (1.80x+): {result}%"
        )
    except Exception as e:
        bot.send_message(message.chat.id, f"Xatolik: {e}")

bot.polling()

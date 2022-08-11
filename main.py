import telebot 
from telebot import types # для указание типов 
import config 
 
bot = telebot.TeleBot("5460720014:AAGTvbQKhzndZfOQMeiZETHr3deswp5nUw4") 

@bot.message_handler(commands=['start']) 
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton("❓ Определить класс") 
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот конференций, нажми на кнопку ниже, чтобы определить твою комнату" .format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text']) 
def func(message) :
    if(message.text == "❓ Определить класс") :

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("📕1 - 4 Класс") 
        btn2 = types.KeyboardButton("📗5 - 8 Класс") 
        btn3 = types.KeyboardButton("📘9 - 11 Класс")
        back = types.KeyboardButton("❌Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)

        bot.send_message(message.chat.id, text="Выбери свой класс", reply_markup=markup)

    elif message.text == "📕1 - 4 Класс":
        bot.send_message(message.chat.id, text ="📕Ваша комната №1, https://t.me/+hxmG20WsVsw1MjBi")
 
     
    elif message.text == "📗5 - 8 Класс":
        bot.send_message(message.chat.id, text="📗Ваша комната №2, https://t.me/+IiVH4WW6tbwzYzYy")

    elif message.text == "📘9 - 11 Класс":
        bot.send_message(message.chat.id, text="📘Ваша комната №3, https://t.me/+Tg0q-VMQy9I2NDRi")
     
    elif (message.text == "❌Вернуться в главное меню"):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        button1 = types.KeyboardButton("❓ Определить класс")         
        markup.add(button1) 
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup) 
    else :
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..") 
 
bot.polling(none_stop=True)

from config import token

import telebot
from PIL import Image, ImageOps
import io
import os
from random import choice
bot = telebot.TeleBot(token)

# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Получаем информацию о фотографии с наивысшим разрешением
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    # Создаем объект изображения из байтов
    image = Image.open(io.BytesIO(downloaded_file))
    
    # Инвертируем цвета изображения
    inverted_image = ImageOps.invert(image)
    
    # Сохраняем обработанное изображение временно
    temp_image_path = "temp_image.jpg"
    inverted_image.save(temp_image_path)
    
    # Отправляем обработанное изображение назад пользователю
    with open(temp_image_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)
    
    # Удаляем временный файл изображения
    os.remove(temp_image_path)


# Handle '/start' and '/help'
@bot.message_handler(commands=['hi', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['info', ])
def send_info(message):
    bot.send_message(message.chat.id, """\
hi am a telegram bot tg bot 3000 i am at beta and i relly can t do anything still """)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])


@bot.message_handler(commands=['stand_for_pvp'])
def coin_handler(message):
    coin = choice(["Anubis ", "King Crimson", "star platinum", "The World ", "stone free", "Whitesnake", "Red Hot Chili Pepper", "Crazy Diamond", "Killer Queen", "Gold Experience", "Silver Chariot", "Hermit Purple", "The Hando", "Purple Haze", "cream", "Hierophant Green", "Magician's Red", "White Album", "Aerosmith", "Six Pistols", "Beach Boy", "Mr. President", "Sticky Fingers", "soft & wet"])
    bot.reply_to(message, coin)


# Запуск бота с бесконечным опросом
bot.infinity_polling()




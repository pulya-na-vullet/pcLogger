import telebot

# Создаем объект бота
bot = telebot.TeleBot("6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw")

# Обработчик нажатия на кнопку "привет"
@bot.message_handler(func=lambda message: message.text == "привет")
def handle_hello(message):
    print("привет")
# Создаем кнопки для inline-клавиатуры
hello_button = telebot.types.InlineKeyboardButton("привет", callback_data="hello")

# Обработчик callback-запросов
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    # Если нажата кнопка "привет", вызываем обработчик нажатия на кнопку "привет"
    if call.data == "hello":
        handle_hello(call.message)
        print("Hi 3")


# Создаем inline-клавиатуру и добавляем в нее кнопки
inline_keyboard = telebot.types.InlineKeyboardMarkup()
inline_keyboard.row(hello_button)
print("Hi 1")

# Отправляем сообщение и inline-клавиатуру пользователю
bot.send_message(781078907, "Нажми кнопку:", reply_markup=inline_keyboard)
print("Hi 2")


# Запускаем бота
bot.polling()


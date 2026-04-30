import telebot
import random

TOKEN = "8788796720:AAGmTJ2eI-m9jtKvnQbS-IFezZuIt_20YNI"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


def format_name(user):
    return user.first_name or "Игрок"


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "<b>Привет!</b>\nДобавь меня в группу и используй /rpcmd"
    )


@bot.message_handler(commands=["rpcmd"])
def rpcmd(message):
    bot.send_message(
        message.chat.id,
        "<b>RP команды:</b>\n\n"
        "<b>/me</b> - действие от первого лица\n"
        "<b>/do</b> - описание окружения или состояния\n"
        "<b>/todo</b> - речь + действие\n"
        "<b>/try</b> - действие с шансом успеха"
    )


@bot.message_handler(commands=["me"])
def me(message):
    text = message.text.replace("/me", "", 1).strip()
    if not text:
        bot.reply_to(message, "<b>Используй:</b> /me зашел в комнату")
        return

    bot.send_message(
        message.chat.id,
        f"<b>{format_name(message.from_user)}</b> - {text}"
    )


@bot.message_handler(commands=["do"])
def do(message):
    text = message.text.replace("/do", "", 1).strip()
    if not text:
        bot.reply_to(message, "<b>Используй:</b> /do Паспорт лежит на столе")
        return

    bot.send_message(
        message.chat.id,
        f"<b>{format_name(message.from_user)}</b> - {text}"
    )


@bot.message_handler(commands=["todo"])
def todo(message):
    text = message.text.replace("/todo", "", 1).strip()
    if not text:
        bot.reply_to(message, "<b>Используй:</b> /todo Здравствуйте! * передавая паспорт")
        return

    if "*" in text:
        speech, action = text.split("*", 1)
        result = f"<b>{format_name(message.from_user)}</b> - {speech.strip()} *{action.strip()}*"
    else:
        result = f"<b>{format_name(message.from_user)}</b> - {text}"

    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["try"])
def try_cmd(message):
    text = message.text.replace("/try", "", 1).strip()
    if not text:
        bot.reply_to(message, "<b>Используй:</b> /try попытался открыть дверь")
        return

    result = random.choice(["Успешно", "Неудачно"])

    bot.send_message(
        message.chat.id,
        f"<b>{format_name(message.from_user)}</b> - {text}\n<b>Результат:</b> {result}"
    )


@bot.message_handler(func=lambda message: message.chat.type == "private")
def private_text(message):
    bot.send_message(
        message.chat.id,
        "<b>Это ЛС RP-бота.</b>\nДобавь меня в группу и используй /rpcmd"
    )


bot.infinity_polling()

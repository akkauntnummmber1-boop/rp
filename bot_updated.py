import telebot
import random

TOKEN = "8788796720:AAGmTJ2eI-m9jtKvnQbS-IFezZuIt_20YNI"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


def format_name(user):
    return user.first_name


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "<b>Привет!</b> Напиши /rpcmd"
    )


@bot.message_handler(commands=["rpcmd"])
def rpcmd(message):
    bot.send_message(
        message.chat.id,
        "<b>RP команды:</b>
"
        "/me /do /todo /try"
    )


@bot.message_handler(commands=["me"])
def me(message):
    text = message.text.replace("/me", "", 1).strip()
    if not text:
        return
    bot.send_message(
        message.chat.id,
        f"<b>{format_name(message.from_user)}</b> - {text}"
    )


@bot.message_handler(commands=["do"])
def do(message):
    text = message.text.replace("/do", "", 1).strip()
    if not text:
        return
    bot.send_message(
        message.chat.id,
        f"<b>{format_name(message.from_user)}</b> - {text}"
    )


@bot.message_handler(commands=["todo"])
def todo(message):
    text = message.text.replace("/todo", "", 1).strip()
    if not text:
        return

    if "*" in text:
        speech, action = text.split("*", 1)
        result = f"<b>{format_name(message.from_user)}</b> - {speech.strip()} ({action.strip()})"
    else:
        result = f"<b>{format_name(message.from_user)}</b> - {text}"

    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["try"])
def try_cmd(message):
    text = message.text.replace("/try", "", 1).strip()
    if not text:
        return

    result = random.choice(["Успешно", "Неудачно"])

    bot.send_message(
        message.chat.id,
        f"<b>{format_name(message.from_user)}</b> - {text} ({result})"
    )


@bot.message_handler(func=lambda message: message.chat.type == "private")
def private_text(message):
    bot.send_message(
        message.chat.id,
        "<b>Это ЛС RP-бота</b>"
    )


bot.infinity_polling()

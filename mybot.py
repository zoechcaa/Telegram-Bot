import telebot
import random

token = ""
bot = telebot.TeleBot(token)

tasks={}
RANDOM_TASKS = ["погладить кота","пойти гулять","прибраться в квартире","полить цветы","проветрить комнату","послушать музыку","посмотреть Веронику Степанову","программировать","сделать зарядку"]
HELP = """
Все доступные команды:
/help - вывести список доступных команд
/add - добавить задачу в to-do лист (/add дата задача)
/show - вывести все задачи на определенную дату (/show дата)
/random - создать случайную задачу на сегодня
Чтобы посмотреть задачи на сегодня - введи /show сегодня
"""

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["start"])
def start(message):
    text="""
    Привет! Для вывода всех доступных команд используй команду /help
    """
    bot.send_message(message.chat.id, text)


def add_todo(day, task):
  if day in tasks:
      tasks[day].append(task)
  else:
      tasks[day] =[]
      tasks[day].append(task)


@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    day = command[1].lower()
    task = command[2]
    add_todo(day, task)
    text = "Задача "+task+" успешно добавлена на дату "+day+"!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    day = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(day,task)
    text = "Задача "+task+" успешно добавлена на дату "+day+"!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    day = command[1].lower()
    if day in tasks:
        text = day.upper()+"\n"
        for task in tasks[day]:
          text = text +"- "+task+"\n"

    else:
      text = "Задач на этот день нет!"
    bot.send_message(message.chat.id, text)


# Постоянно обращается к серверам телеграма
bot.polling(none_stop=True)
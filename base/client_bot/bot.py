from bitly_check import count_clicks

from telegram.ext import Updater, CommandHandler
from environs import Env

env = Env()
env.read_env()


def start(update, context):
    text = 'Привет! Введите /comands для просмотра моих команд .'
    context.bot.send_message(
            chat_id=update.effective_chat.id, text=text
    )
   

def comands(update, context):
    text = '/check - количество переходов по рекламе\n/sum - сумма заказов'
    context.bot.send_message(
            chat_id=update.effective_chat.id, text=text
    )


def check(update, context):
    url = 'https://bit.ly/3AEtprS'
    bitly_token = env.str('BITLY_TOKEN')
    count = count_clicks(bitly_token, url)
    text = f'Количество переходов {count}'
    context.bot.send_message(
            chat_id=update.effective_chat.id, text=text
    )


def main():
    telegram_token = env.str('TELEGRAM_TOKEN')

    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    comands_handler = CommandHandler('comands', comands)
    dispatcher.add_handler(comands_handler)

    check_handler = CommandHandler('check', check)
    dispatcher.add_handler(check_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
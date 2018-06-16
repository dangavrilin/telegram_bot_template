import config
import telebot
import logging
from flask import Flask, request, abort

bot = telebot.TeleBot(config.token)

app = Flask(__name__)


def set_logger():
    if config.log_level == 'DEBUG':
        telebot.logger.setLevel(logging.DEBUG)
    elif config.log_level == 'INFO':
        telebot.logger.setLevel(logging.INFO)
    else:
        pass


# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return '^._.^'


# Process webhook calls
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am EchoBot!")


# Handle all other messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    app.run(host=config.listen,
            port=config.port,
            debug=True)

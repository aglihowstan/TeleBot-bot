import telebot
from telebot import types
from time import sleep

# replace CAPITAL WORDS with your values

bot=telebot.TeleBot('BOT TOKEN')

# CREATING THE /START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    photo = open('FILE', 'br')
    markup=types.InlineKeyboardMarkup()
    btn=types.InlineKeyboardButton('watch', callback_data='delmess')
    markup.row(btn)
    bot.send_photo(message.chat.id, photo,  "<b>watch all series</b>", parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delmess':
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1 series', callback_data='delmess2')
        markup1.add(btn1)

        btn2 = types.InlineKeyboardButton('2 series', callback_data='delmess2')
        markup1.add(btn2)

        btn3 = types.InlineKeyboardButton('3 series', callback_data='delmess2')
        markup1.add(btn3)

        btn4 = types.InlineKeyboardButton('4 series', callback_data='delmess2')
        markup1.add(btn4)

        btn5 = types.InlineKeyboardButton('5 series', callback_data='delmess2')
        markup1.add(btn5)

        btn6 = types.InlineKeyboardButton('6 series', callback_data='delmess2')
        markup1.add(btn6)

        btn7 = types.InlineKeyboardButton('7 series', callback_data='delmess2')
        markup1.add(btn7)

        btn8 = types.InlineKeyboardButton('8 series', callback_data='delmess2')
        markup1.add(btn8)

        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "<b>select series:</b>", parse_mode='html', reply_markup=markup1)

    if callback.data == 'delmess2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        markup2 = types.InlineKeyboardMarkup()
        btn10 = types.InlineKeyboardButton('confirm', callback_data='delmess3')
        markup2.add(btn10)
        bot.send_message(callback.message.chat.id, "Please subscribe to the channels:\n1. fisrt channel\n2. second channel",parse_mode='html', reply_markup=markup2)

# SUBSCRIPTION VERIFICATION

    if callback.data == 'delmess3':
        res = bot.get_chat_member('CHANNEL ID', callback.message.chat.id)
        res2 = bot.get_chat_member('CHANNEL ID', callback.message.chat.id)

        # IF THE USER IS SUBSCRIBED TO CHANNELS, THE BOT WILL SEND HIM A CHANNEL
        if (res.status == 'member' and res2.status == 'member'):
            bot.delete_message(callback.message.chat.id, callback.message.message_id)
            bot.send_message(callback.message.chat.id,"Cheking subscriprions..")
            sleep(5)
            bot.send_message(callback.message.chat.id,"<b>You can watch all the episodes here:\nCHANNEL ADRESS",parse_mode='html')

        # IF THE USER IS NOT SUBSCRIBED TO CHANNELS THE MESSAGE WILL BE RETURNED
        else:
            bot.delete_message(callback.message.chat.id, callback.message.message_id)
            markup3=types.InlineKeyboardMarkup()
            btn11=types.InlineKeyboardButton('confrim', callback_data='del3')
            markup3.add(btn11)
            bot.send_message(callback.message.chat.id, "Please subscribe to the channels:\n1. fisrt channel\n2. second channel",parse_mode='html', reply_markup=markup3)
            
# IF THE USER SENDS A MESSAGE THAT IS NOT PROCESSED BY THE BOT
@bot.message_handler()
def user_unknown_text(message):
    bot.send_message(message.chat.id, "Write <b>/start</b> or <b>select the button</b>", parse_mode='html')

bot.polling(none_stop=True)
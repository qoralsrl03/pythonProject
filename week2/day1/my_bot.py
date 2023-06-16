#-*- coding:utf-8 -*-
#pip install python-telegram-bot==13.11
import os
import random

import telegram
import datetime
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext, commandhandler, CommandHandler

print(telegram.__version__)
KEY="6036344403:AAGQvjoVajMtUf2OzCplx2VobKzxi8uDn_U"
updater = Updater(token=KEY, use_context=True)
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id=user_id, text=user_text)

img_dir = './images/'
file_dir = './files/'
diary_dir = './diaries/'
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
if not os.path.exists(file_dir):
    os.mkdir(file_dir)
if not os.path.exists(diary_dir):
    os.mkdir(diary_dir)

def get_photo(update, context:CallbackContext):
    print('get photo')
    #현재 날짜와 시간
    now = datetime.datetime.now()
    now_yyyymmdd = now.strftime('%Y-%m-%d %H:%M:%S')
    file_path = os.path.join(img_dir, now_yyyymmdd+'.png')
    bot = context.bot
    photo = bot.getFile(update.message.photo[-1].file_id)
    photo.download(file_path)
    update.message.reply_text('photo saved:' + file_path)

def get_lotto(update, context):
    arr = []
    print('make lotto')
    user_id = update.effective_chat.id
    user_text = update.message.text
    cnt = int(user_text.replace('/lotto', '').strip())
    print(cnt, '개 생성')
    for v in range(cnt):
        com_set = set()
        while True:
            com_set.add(random.randint(1, 45))
            if len(com_set) == 6:
                arr.append(list(com_set)) #set 객체는 JSON으로 직렬화가 불가능하여 리스트로 변환한다음 arr에 추가해야함
                break
    print('-' * 100)
    user_id = update.effective_chat.id
    user_text = str(cnt) + '개 생성'
    context.bot.send_message(chat_id=user_id, text=user_text)
    for i in range(cnt):
        user_id = update.effective_chat.id
        user_text = arr[i]
        context.bot.send_message(chat_id=user_id, text=user_text)
        print(arr[i])

def get_file(update, context:CallbackContext):
    message = update.effective_message
    bot = context.bot
    if message.document is not None:
        file_id_short = message.document.file_id
        file_url = os.path.join(file_dir,message.document.file_name)
        bot.getFile(file_id_short).download(file_url)
        message.reply_text('file save:' + file_url)

# def fn_diary(update, context):
#     print('diary!!')
#     file = 'diary.txt'
#     f = open(file, 'a')  # a append, r read, w write
#     user_id = update.effective_chat.id
#     context.bot.send_message(chat_id=user_id, text='할 말을 입력하세요 : ')
#     while True:
#         user_text = update.message.text
#         print(user_text)
#         context.bot.send_message(chat_id=user_id, text=user_text)
#         if 'q' == user_text:
#             break
#         f.write(user_text)
#         f.write('\n')  # 개행 문자('\n') 추가
#         updates = context.bot.get_updates()
#         if updates:
#             update = updates[0].message
#     f.close()


# diary_handler = CommandHandler('diary',fn_diary)
# updater.dispatcher.add_handler(diary_handler)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

lotto_handler = CommandHandler('lotto', get_lotto) #/lotto 3
updater.dispatcher.add_handler(lotto_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)
updater.start_polling()
updater.idle()

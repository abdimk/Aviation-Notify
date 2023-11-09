import os
import asyncio
import time
from pathlib import Path
from pyrogram import Client,filters
from os import listdir
from os.path import isfile, join
from config import API_HASH, API_ID, BOT_TOKEN

Channel_id = -1001845353675

bot = Client(
    "Opensky_sesstion",
    api_id = ,
    api_hash = "",
    bot_token= "16Pc"
)

@bot.on_message(filters.command('start')&filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id,"Hello am simple bot!")

os.chdir('images')
@bot.on_message(filters.command('start') & filters.channel)
def command2(bot, message):
    bot.send_message(message.chat.id,"started...")
    mypath = Path('images')
    images = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for image in images:
        time.sleep(10)
        bot.send_photo(message.chat.id,f"{image}",caption=f"**{image}**")
    print('done..')
    
print('listing...')
bot.run()
 

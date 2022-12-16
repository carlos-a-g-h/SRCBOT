#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28089894
API_HASH = "e9e8713438c69f8d2b3149eef8fc7b5d"
BOT_TOKEN = "5472838925:AAHEYmCYigqYyl4TYv8DN2A_nipTIryTSJw"
SESSION = "AQGsniYASnIu2PlSMynHl6jhp1_ZODtHQWu5Q0O8I1wVi_RMJeX-anfoWmMBIMxB1AzaDWwCl5IuXzz9_AjXS7kfOOHLZsuIVFoJC9llnKOm5SE861DrHy9aKbQRULQJzdi8dePFAwmX5kJ33HHAF39vcEU6XeB4H7_hsg3zlwQsE6jFctLwVsseynQGgpnqIT0mb7S_cmcOsARdecOjYdK3r1AZRVsZE-_yo494xj5xuOl_SPaJQEalxiNYRZbSMTo001W1Tp4GCIrPSH9yDSVHy5xulQg0I8sQ7jyEVfoyIyNqUNHLzYkFp6WoVByZlrLq5fQrmZQ5Pzly8v_24BoxVqwiQAAAAAFa60aNAA"
FORCESUB = "saverestrictedc"
AUTH = "5074781537"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

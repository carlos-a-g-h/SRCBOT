#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, os, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION = os.getenv("SESSION")
FORCESUB = os.getenv("FORCESUB")
AUTH = os.getenv("AUTH")

# API_ID = 9050192
# API_HASH = "73c4c8292bdfd6a90589049864ebbb34"
# BOT_TOKEN = "5472838925:AAHEYmCYigqYyl4TYv8DN2A_nipTIryTSJw"
# SESSION = "AQCKGFAAcA7WQVQe-N46it6cYsuVN5m7oGPFkpJtwJLiuLAxeT4wc53fAzd3vNB6NV5RGaQFW9N9FP_fjLIJ3-eOmZ6iCUWkLZqEKOy_nJNPeeMD6AEM8oZF2_HNvo0PW0La8HL63rLtjxm2duPNN8pY6g32U8Z6UlE2w7saFzq_FndnEAEoZKEq1riyB-uwik7EMrOz5UbAV44HMiLbkbyO8NS_B304XNjCHseLGRBWbVptdBE0pZoK3yOBeUB8Nbe11b9HkS--2lQwQ7pOpWJP6IFKJkxATjdIH2QcNPHDcrDQ7hmonSKjN-LwX5nqF2nyH-YY6XVdn2nWSrLM_JSGI3WAkgAAAAEuewVhAA"
# FORCESUB = "SyP_Leech"
# AUTH = "5074781537"

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

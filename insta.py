import os
import time
import Config # Check karein agar aapki file ka naam Config.py hai ya config.py
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(level=logging.WARNING)

# Time synchronization ke liye wait
time.sleep(10)

app = Client(
    "InstagramBotSession", 
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Instaloader"),
    workdir="./" 
)

if __name__ == "__main__":
    try:
        app.start()
        # Ab bot pehle start hoga, phir username check karega
        me = app.get_me()
        print(f"@{me.username} Started Successfully!")
        idle()
    except Exception as e:
        print(f"Bot failed to start: {e}")
    finally:
        if app.is_connected:
            app.stop()

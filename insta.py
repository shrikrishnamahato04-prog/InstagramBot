import os
import time
import Config 
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(level=logging.WARNING)

# FIX: Time sync ke liye 15 second ka wait
time.sleep(15)

app = Client(
    "InstaBot_Final_Sync", # FIX: Naya session name
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Instaloader"),
    workdir="./",
    sleep_threshold=120 
)

if __name__ == "__main__":
    try:
        app.start()
        me = app.get_me()
        print(f"@{me.username} Started Successfully!")
        idle()
    except Exception as e:
        print(f"Bot failed to start: {e}")
    finally:
        if app.is_connected:
            app.stop()

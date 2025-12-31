import os
import time
import Config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Logging setup
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Bot ko start hone se pehle 10 second ka wait dene ke liye taaki clock sync ho jaye
print("Waiting for 10 seconds to sync system clock...")
time.sleep(10)

# Client Setup: ":memory:" ko hata kar fix session name dala hai
app = Client(
    "InstagramBotSession", 
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Instaloader"),
    workdir="./" 
)

# Run Bot Logic
if __name__ == "__main__":
    try:
        print("Starting Bot...")
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        print(f"Error occurred: {e}")
        
    uname = app.get_me().username
    print(f"@{uname} Started Successfully!")
    idle()
    app.stop()
    print("Bot stopped. Alvida!")

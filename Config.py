import os

# Maine fix kar diya hai taaki ye seedha Heroku Config Vars se data le
API_ID = int(os.environ.get('API_ID', 0))
API_HASH = os.environ.get('API_HASH', None)
BOT_TOKEN = os.environ.get('BOT_TOKEN', None)

# Database URL fix (Jo aapke code mein tha wahi hai, bas format sahi kiya hai)
DATABASE_URL = os.environ.get('DATABASE_URL', "")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Must Join Logic (Wahi same logic jo aapne diya tha)
MUST_JOIN = os.environ.get('MUST_JOIN', "StarkBots")
if MUST_JOIN and MUST_JOIN.startswith("@"):
    MUST_JOIN = MUST_JOIN.replace("@", "")

# Instagram Credentials
INSTA_USERNAME = os.environ.get('INSTA_USERNAME', None)
INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD', None)

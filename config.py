import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22565342
API_HASH = "75e035926f72f2f4155a6f5f6e64be03"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7201420162:AAEN0tjOZ0q-3xKjyqRZf7CMxFkL6FjLhXQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = "-1002666719095"

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = "7926944005"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gxinfinity/AvonMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/gxinfinity_support"
SUPPORT_GROUP = "https://t.me/infinitygx_bot_support"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION1", "BQFYUd4Awi4oQx8mqn94Z1gtZHxnZbfA_5dPXZv23LuWCZXH3rPMUUHAsFl-FH7CH2qVETgbpjiKMZ_KwjsO2cyuene_iUvqlTuDVfjMAv9oTTjA7gh3IUtGcIMngIymazZn55ujq770DiFnnFfuom6x3vxo8v3VkMQDPpE0_bJYb678VIE19lvM_saF0TYXqw5iH81yP2RhVTxJltlG7fWkJyKOBnGgI9jNX4A0T33WNnunZE7lvVqZp_1_luvfP0tw2nx7RsbO-hFb5r7loKn5Id0h9DJVFIbLvfcxhpcIbwPZMleVnUkobUAu9pNTxXHyy1igi_fRuenQfDmHASRWZm01CQAAAAGJKA9qAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://telegra.ph/file/d6e41e4ec944ac5005171.jpg"

PING_IMG_URL = "https://graph.org/file/a91c82c2e312a56d2db4e-e60a99710077dbdd38.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/a91c82c2e312a56d2db4e-e60a99710077dbdd38.jpg"
STATS_IMG_URL = "https://graph.org/file/a91c82c2e312a56d2db4e-e60a99710077dbdd38.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )

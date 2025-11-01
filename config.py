# Config file for Telegram File Sharing Bot
# Customized & maintained by @alexdrvfreak
# Example channel: https://t.me/examplechannel
# Example support: https://t.me/example_support

import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
# Bot credentials
TG_BOT_TOKEN = os.environ.get("8222645012:AAEQMNK31oa5hDo_9OEStfNL7FMBdZMkUFM", "")
APP_ID = int(os.environ.get("29167872", ""))  # Your API ID from my.telegram.org
API_HASH = os.environ.get("f26b4e46f6d6e5ad36f480e73357425d", "")   # Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003292247930"))  # Your DB channel ID
OWNER = os.environ.get("OWNER", "AlphaX_07")                   # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7681308594"))           # Owner Telegram ID
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/example_support")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://example.com/start.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://example.com/force.jpg")
#--------------------------------------------

HELP_TXT = """<b><blockquote>
This is a File to Link Bot.

❏ Bot Commands
├ /start : Start the bot
├ /about : About us
└ /help : Show this help

Developed by <a href="https://t.me/alexdrvfreak">alexdrvfreak</a>
</blockquote></b>"""

ABOUT_TXT = """<b><blockquote>
◈ Creator: <a href="https://t.me/alexdrvfreak">alexdrvfreak</a>
◈ Example Channel: <a href="https://t.me/examplechannel">My Channel</a>
◈ Support: <a href="https://t.me/example_support">Support Group</a>
</blockquote></b>"""
#--------------------------------------------

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}\n\n<blockquote>I am a File Store Bot. I can save private files in a channel and give you special access links.</blockquote></b>"
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {first}\n\n<b>Please join our channels and then click on the reload button to get your requested file.</b>"
)

CMD_TXT = """<blockquote><b>» Admin Commands:</b></blockquote>

<b>›› /dlt_time :</b> Set auto delete time
<b>›› /check_dlt_time :</b> Check current delete time
<b>›› /dbroadcast :</b> Broadcast document / video
<b>›› /ban :</b> Ban a user
<b>›› /unban :</b> Unban a user
<b>›› /banlist :</b> Get list of banned users
<b>›› /addchnl :</b> Add force-sub channel
<b>›› /delchnl :</b> Remove force-sub channel
<b>›› /listchnl :</b> View added channels
<b>›› /fsub_mode :</b> Toggle force-sub mode
<b>›› /pbroadcast :</b> Send photo to all users
<b>›› /add_admin :</b> Add an admin
<b>›› /deladmin :</b> Remove an admin
<b>›› /admins :</b> Get list of admins
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• by @alexdrvfreak</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
#--------------------------------------------
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "You are not authorized to use this command!"
#--------------------------------------------

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

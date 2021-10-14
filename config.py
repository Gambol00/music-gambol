import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ɢ8 ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ab2c87e2a01a9bd222d1f.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/ab2c87e2a01a9bd222d1f.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/ab2c87e2a01a9bd222d1f.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/ab2c87e2a01a9bd222d1f.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "G8_00_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "G8_00_0")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "G8_00L")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G8_01")
OWNER_NAME = getenv("OWNER_NAME", "G8_M_L") 
DEV_NAME = getenv("DEV_NAME", "G8_M_L")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Credits Logs @BianSepang , @KenHV
# Ported @Badboyanim
"""Userbot initialization."""

import signal
import os
import time
import re
import io
import random

from datetime import datetime
from time import sleep
from platform import python_version
from telethon import TelegramClient, version
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon.sync import custom, events
from telethon.sessions import StringSession
from telethon import Button, functions, types
from telethon.utils import get_display_name

load_dotenv("config.env")

StartTime = time.time()

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("You MUST have a python version of at least 3.8."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Custom Module
CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)

# Pm Permit Img
PM_PERMIT_PIC = os.environ.get(
    "PM_PERMIT_PIC",
    None) or "https://telegra.ph/file/7e2f02c9ed20a81481dc4.jpg"

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/aryazakaria01/CyberDyne-Userbot")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "CyberDyne-Userbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# DEVELOPER and SUDO_USERS
DEVELOPER = 1345333945, 1448477501, 1682708454, 1276135372, 1663258664
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", None)

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "7.0")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO",
    None) or "https://telegra.ph/file/7e2f02c9ed20a81481dc4.jpg"

# Link Instagram for CMD Alive
INSTAGRAM_ALIVE = os.environ.get(
    "INSTAGRAM_ALIVE") or "instagram.com/geezingsupport"

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)

lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except Exception:
        pass

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
G_DRIVE_INDEX_URL = os.environ.get("G_DRIVE_INDEX_URL", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY", "./downloads")

# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius Lyrics  API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# IMG Stuff
IMG_LIMIT = os.environ.get("IMG_LIMIT", None)

CMD_HELP = {}

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID", None)

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Uptobox
USR_TOKEN = os.environ.get("USR_TOKEN_UPTOBOX", None)


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)


def shutdown_bot(signum, frame):
    LOGS.info("Received SIGTERM.")
    bot.disconnect()
    sys.exit(143)


signal.signal(signal.SIGTERM, shutdown_bot)


def migration_workaround():
    try:
        from userbot.modules.sql_helper.globals import addgvar, delgvar, gvarstatus
    except AttributeError:
        return None

    old_ip = gvarstatus("public_ip")
    new_ip = get("https://api.ipify.org").text

    if old_ip is None:
        delgvar("public_ip")
        addgvar("public_ip", new_ip)
        return None

    if old_ip == new_ip:
        return None

    sleep_time = 180
    LOGS.info(
        f"A change in IP address is detected, waiting for {sleep_time / 60} minutes before starting the bot."
    )
    sleep(sleep_time)
    LOGS.info("Starting bot...")

    delgvar("public_ip")
    addgvar("public_ip", new_ip)
    return None


# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)


async def update_restart_msg(chat_id, msg_id):
    DEFAULTUSER = ALIVE_NAME or "Set `ALIVE_NAME` ConfigVar!"
    message = (
        f"**⚡ℂ𝕪𝕓𝕖𝕣𝔻𝕪𝕟𝕖-𝕌𝕤𝕖𝕣𝕓𝕠𝕥⚡ 𝖎𝖘 𝕭𝖆𝖈𝖐 𝖀𝖕 𝖆𝖓𝖉 𝕽𝖚𝖓𝖓𝖎𝖓𝖌!**\n\n"
        f"⚙️ **𝕿𝖊𝖑𝖊𝖙𝖍𝖔𝖓 :** __{version.__version__}__\n"
        f"🐍 **𝕻𝖞𝖍𝖙𝖔𝖓 :** __{python_version()}__\n"
        f"👤 **𝖀𝖘𝖊𝖗 :** __{DEFAULTUSER}__"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from userbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    try:
        with bot:
            bot.loop.run_until_complete(
                update_restart_msg(
                    int(chat_id), int(msg_id)))
    except BaseException:
        pass
    delgvar("restartstatus")
except AttributeError:
    pass


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}

# Import Userbot - Ported by KENZO

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 4
    number_of_cols = 2
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline("{} {} 」◑".format("◐「", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⋖╯Pʀᴇᴠ", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "ᴄʟᴏꜱᴇ", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "Nᴇxᴛ╰⋗", data="{}_next({})".format(prefix, modulo_page)
                )
            )
        ]
    return pairs


with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id

        aliplogo = "https://telegra.ph/file/b6580efa28fdc144749d5.jpg"
        lynxlogo = "resource/logo/CyberDyneUserbot-Button.jpg"
        plugins = CMD_HELP

        @tgbot.on(events.NewMessage(pattern=r"/start"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"Hai 👋 [{get_display_name(u)}](tg://user?id={u.id}) Selamat Datang di ⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭⚡\nJika Kalian Datang Kesini dan Ingin Mengetahui CyberDyne-Robot Lebih Lanjut,\nSilahkan Pilih **Menu Bantuan** Dibawah Ini.\n",
                    buttons=[
                        [
                            Button.url("📢 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 📢",
                                       "t.me/Lunatic0de"),
                            Button.url("🚨 𝗠𝗲𝗻𝘂-𝗕𝗮𝗻𝘁𝘂𝗮𝗻 🚨",
                                       "https://telegra.ph/Bantuan-06-11")],
                        [Button.url("👤 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 👤",
                                    "t.me/GeezSupportGroup")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern=r"/deploy"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.reply(
                    '⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭⚡ Deploy to Heroku, Click Here 👇🏻',
                    buttons=[
                        [
                            Button.url(
                                "⚒️ 𝗗𝗘𝗣𝗟𝗢𝗬 ⚒️",
                                "https://heroku.com/deploy?template=https://github.com/aryazakaria01/Stephanie-Userbot/tree/Stephanie-Userbot",
                            )
                        ],
                        [Button.url("👥 𝗚𝗥𝗢𝗨𝗣 👥", "t.me/NatsunagiCorporationGroup")],
                    ],
                )

        @tgbot.on(events.NewMessage(pattern=r"/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                text = (
                    f"Haii 😼 [{get_display_name(u)}](tg://user?id={u.id}) My Name is 𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞 🐈\n"
                    f"CyberDyne Used For Fun On Telegram✨,\n"
                    f"and For Maintaining Your Group 🛠️.\n"
                    f"I was **Created by :** @Badboyanim For Various Userbots on Github.\n")
                await tgbot.send_file(event.chat_id, file=lynxlogo,
                                      caption=text,
                                      buttons=[
                                          [
                                              custom.Button.url(
                                                  text="🇮🇩 𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆 🇮🇩",
                                                  url="https://aryazakaria01.github.io/CyberDyne-Userbot/"
                                              )
                                          ]
                                      ]
                                      )

        @tgbot.on(events.NewMessage(pattern=r"/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG !!**\n `{ms}ms`",
                )

        @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@LynxRobot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=lynxlogo,
                    link_preview=False,
                    text=f"\n**Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n\n◎› **Bᴏᴛ ᴠᴇʀ :** `v.{BOT_VER}`\n◎› **Pʟᴜɢɪɴꜱ :** `{len(plugins)}`\n\n**Cᴏᴘʏʀɪɢʜᴛ © 𝟤𝟢𝟤𝟣 ᴄʏʙᴇʀᴅʏɴᴇ-Uꜱᴇʀʙᴏᴛ**".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan Dari ⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡ ",
                    text="Daftar Plugins",
                    buttons=[],
                    link_preview=False)
            else:
                result = builder.article(
                    " ╔╡⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭⚡╞╗ ",
                    text="""**Anda Bisa Membuat ⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭⚡ Anda Sendiri\nDengan Cara :**__Tekan Dibawah Ini__ 👇""",
                    buttons=[
                        [
                            custom.Button.url(
                                "⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞⚡",
                                "https://aryazakaria01.github.io/CyberDyne-Userbot"),
                            custom.Button.url(
                                "Dᴇᴠᴇʟᴏᴘᴇʀ",
                                "t.me/GeezSupportGroup")]],
                    link_preview=True,
                )
            await event.answer([result] if result else None)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # Lynx-Openeer
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=aliplogo,
                    link_preview=True,
                    buttons=[
                        [Button.url("⚡𝐂𝐲𝐛𝐞𝐫𝐃𝐲𝐧𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭⚡", "t.me/Badboyanim01_bot")],
                        [Button.url("[⊙] 𝗠𝘆 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺", f"{INSTAGRAM_ALIVE}")],
                    ]
                )
                await event.delete()

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(b"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace('`', '')[:150] + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} Tidak Ada Document Yang Tertulis Untuk Plugin".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Pergi Ke @BotFather Lalu, Settings Bot > Pilih Mode Inline > Turn On."
        )

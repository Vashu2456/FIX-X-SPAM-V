import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from FIXXSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    FIXX_IMG = ALIVE_IMG
else:
    FIXX_IMG = "https://telegra.ph/file/6368cf50226f851cf12b0.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME = "VASHU"

OWNER_ID = config.OWNER_ID

FIXX_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/demon_squad_help_desk"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/chat_group_003")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "@string_session_v_bot")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[『𝐕𝐀𝐒𝐇𝐔』| ͢ ̶ͥ ̶ ̶ͣ ͓ ̶ͫ 𝐕𝐀𝐒𝐇𝐔𓄂⌂🔱 𝐕 ❤️ 𝐅](tg://user?id={1321796330})"
        DEADLY_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs ꜰɪx x ꜱᴘᴀᴍ sᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {creator}!

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {myOwner}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {creator}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, FIXX_IMG, caption=FIXX_ON, buttons=FIXX_Button

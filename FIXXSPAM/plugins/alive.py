import config
from FIXXSPAM import BOT0, FIXXSPAMversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    FIXXSPAM_PIC = PIC
else:
    FIXXSPAM_PIC = "https://telegra.ph/file/00d1648fef96dbb1e3225.jpg"

hl = config.CMD_HNDLR


FIXXSPAM = "✯  𝐕𝐀𝐒𝐇𝐔 𝐗 𝐅𝐈𝐗 𝐒𝐏𝐀𝐌  ✯\n\n"
FIXXSPAM += f"═══════════════════\n"
FIXXSPAM += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
FIXXSPAM += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
FIXXSPAM += f"• **ᴠᴀꜱʜᴜ x ᴋᴀ ᴠᴇʀsɪᴏɴ**  : `{fixxversion}`\n"
FIXXSPAM += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/demon_squad_help_desk"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/DEMONSQUAD001")], [Button.url("• ʀᴇᴘᴏ •", "https://t.me/chat_group_003")]]
     await BOT0.send_file(event.chat_id, FIXXSPAM_PIC, caption=FIXXSPAM, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴠᴀꜱʜᴜ x ꜰɪx ꜱᴘᴀᴍ !**") 

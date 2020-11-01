"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @reeshu_xd
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/b8324f81fb4176ff8494d.jpg"
pm_caption = "**This is GodHackerz Userbot**\n\n"

pm_caption += "Hey Sir! I am Alive. All functions are working properly.\n\n"
pm_caption += "⚡️Status⚡️\n\n"
pm_caption += "😎Telethon Version : (6.0.4)\n"
pm_caption += "🥳Python : (4.0)\n"
pm_caption += "😮 Version : (1.0)\n"
pm_caption += "😱 Sudo : (enabled For Master)\n"
pm_caption += "🤫Database status : All Good\n"
pm_caption += f"🤖 My Pro Master : {DEFAULTUSER}\n\n"
pm_caption += "🤖[✅ Deploy Me Now ✅](https://github.com/rohithaditya/Godhackerz-userbot.git)\n\n"
pm_caption += "🙏[My Creator](t.me/rohithaditya)\n\n"
pm_caption += "🙏Join [Channel](https://t.me/Godhackerzuserbot) For Latest Updates"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

###Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you.
###IMG CREDITS: @reeshu_xd
###Idea by : @ProgrammingError
###Given By : @The_Siddharth_Nigam
### thanks to Rangrok 
### Permission Seeked And Approved 
### Kangers Copy With Full Text 
### thanks To Sipak Bro
###Thanks To Him
###Thanks to him 
###Recoded by @Private_45
###© @Godhackerzuserbot

import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "GodHackerz User"

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/2c2b7a903649303a22010.jpg"
file2 = "https://telegra.ph/file/29072e311e101e7805fb2.jpg"
file3 = "https://telegra.ph/file/a386f6da7009a432f8706.jpg"
file4 = "https://telegra.ph/file/e080376d79ad6d4b49537.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "**This is GodHackerz Userbot**\n\n"

pm_caption += "Hi THERE 👋 MASTER ! I am Alive. All functions are working properly.\n\n"
pm_caption += "⚡️Status⚡️\n\n"
pm_caption += "😎Telethon Version : (1.16.04)\n"
pm_caption += "🥳Python : (3.8.3)\n"
pm_caption += "😮Version : (1.0)\n"
pm_caption += "🥱A.I Verision : Beta **1.0.01** [Ask Support Group Master](t.me/Godhackerzuserbot)\n"
pm_caption += "😱Sudo : **{sudo}**\n"
pm_caption += "🤫Database status : All Fine👌\n"
pm_caption += f"🥰My Pro Master : {DEFAULTUSER}\n\n"
pm_caption += "🤖[✅ Deploy Me Now ✅](https://github.com/rohithaditya/Godhackerz-userbot.git)\n\n"
pm_caption += "© [GodHackerz Userbot](https://github.com/rohithaditya/Godhackerz-userbot/blob/main/LICENSE)\n\n"
pm_caption += "    [GODHACKERZ](https://t.me/Godhackerzuserbot) For Latest Updates\n\n"
pm_caption += "SYSTEM HEALTH : STABLE 😎👍 "

@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

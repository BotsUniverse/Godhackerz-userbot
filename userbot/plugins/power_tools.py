# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
"""
(C) @Godhackerzuserbot
This Is The power tools of userbot
copying must have the below lines
wrote by @Rohithaditya
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown
.cpu
"""

from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd, edit_or_reply
from datetime import datetime
import time
from userbot import Lastupdate

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time




# RESTART CMD
@borg.on(admin_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
     await asyncio.sleep(3)
     await event.edit("Restarting [██░] ...\n`.ping` or `.help` to check if I am online Master")
     await asyncio.sleep(4)
     await event.edit("Restarting [███]...\n`.ping`  or `.help` to check if I am online Master")
     await asyncio.sleep(5)
     await event.edit("Restarted. `.alive` me or `.help` to check if I am online Master")
     await borg.disconnect()
     # https://archive.is/im3rt
     os.execl(sys.executable, sys.executable, *sys.argv)
     # You probably don't need it but whatever
     quit()

# SWITCHOFF CMD
@borg.on(admin_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("😩😩😩😩😩Master U Switched Off Me Master 😞😞/n..Manually turn me on later On My Mother(I Mean Heroku)😑")
    await borg.disconnect()
    
# CPU CMD 
@borg.on(admin_cmd(pattern="cpu"))
async def _(event):
      ubizbest = await edit_or_reply(event, "`<^^^^^>`")
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await ubizbest.edit(f" HELLO MASTER!!! /n ➲ Average System Speed Is `{ms}` \n ➲ Using ME Is `{uptime}`/n DB SERVER IS HEROKU")


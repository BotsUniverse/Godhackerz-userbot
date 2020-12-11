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
# RESTART CMD
@borg.on(admin_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    await event.edit("Restarted. `.ping` me or `.helpme` to check if I am online")
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
    

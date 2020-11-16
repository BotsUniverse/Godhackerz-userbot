"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd




@borg.on(admin_cmd(pattern=r"hack"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    await event.edit("Hacking..")

    # Coded by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo


from telethon import events
import asyncio
from userbot.utils import admin_cmd

@borg.on(admin_cmd("termhack"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0,11)
    await event.edit("`Starting ...`")
    animation_chars = [
            "`root@anon:~# `",
            "`root@anon:~# ls`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~#`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# `",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`\n`victim detected as `**NOOB**` in ghost ...`",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`\n`victim detected as `**NOOB**` in ghost ...`\n\n**All Done!**",
            "`root@anon:~# ls`\n\n**  usr  ghost  codes  **\n\n`root@aono:~# # So Let's Hack it ...`\n`root@anon:~# touch setup.py`\n\n**setup.py deployed ...**\n**Auto CMD deployed ...**\n\n`root@anon:~# trap whoami`\n\n**whoami=**`admin`\n`boost_trap on force ...`\n`victim detected as `**NOOB**` in ghost ...`\n\n**All Done!**\n**Hacked!**\n**Token=**`DJ65gulO90P90nlkm65dRfc8I`",
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11]) = [
        
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Targeted Account Hacked...\n\nPay 69$ To Remove this hack..`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])

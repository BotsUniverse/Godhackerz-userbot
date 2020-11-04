# Plugin To Install Plugins 
# We Are Not Responsible If Userbot Got Crashed 
# © @Godhackerzuserbot

from userbot.utils import admin_cmd, load_module, remove_plugin
import asyncio
import os
from datetime import datetime
from pathlib import Path
DELETE_TIMEOUT = 5

@borg.on(admin_cmd(pattern="load", outgoing=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "Master I Have Installed This Plugin`{}` Sucessfully.".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "Error Had Occurring Master,This plugin is already installed/pre-installed Master.If You Find Errors plz Report to @Godhackerzuserbot"
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

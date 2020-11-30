from userbot import bot
from telethon import events
from userbot.utils import command, remove_plugin, load_module
from var import Var
import importlib
from pathlib import Path
from userbot import LOAD_PLUG
import sys
from userbot import ALIVE_NAME
import asyncio
import traceback
import os
import userbot.utils
from datetime import datetime
from userbot.utils import edit_or_reply as eor

DELETE_TIMEOUT = 8
thumb_image_path = "./resources/1207066133.png"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "GodhackerzUserbot"

@command(pattern="^.load", outgoing=True)
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
                await eor(
                    event,
                    "Plugin successfully installed\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "**Error!**\nPlugin cannot be installed Master!\n Or may have been pre-installed Master. If You Find Any Error Then Go To [Support Group](t.me/Godhackerzuserbot) Master",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@command(pattern="^.give (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    sob = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**>>> Plugin name:** `{input_str}`\n**>>>Uploaded in {time_taken_in_ms} seconds only.**\n**>>> Uploaded by:** [{DEFAULTUSER}](tg://user?id={sob})\n**© @Godhackerzuserbot**\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await eor(event, "**Error 404**: :( File Not Found :(")


@command(pattern="^.remove (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f"Master I Have Successfully unloaded {shortname} This Stupid Plugin")
    except Exception as e:
        await qwe.edit(
            "Master I Have Successfully unloaded {shortname}\n{} This Plugin".format(shortname, str(e))
        )

@command(pattern="^.load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await qwe.edit(
            f"Master I could not load {shortname} because of the following error.\n{str(e)}"
        )

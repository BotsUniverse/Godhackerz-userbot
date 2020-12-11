from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from var import Var

@borg.on(admin_cmd(pattern="xo$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    yt = "play"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, yt) 
    await tap[0].click(event.chat_id)
    await event.delete()
	
	
@borg.on(admin_cmd(pattern="wspr ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    rohith = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, rohith) 
    await tap[0].click(event.chat_id)
    await event.delete()
	
	
@borg.on(admin_cmd(pattern="app ?(.*)"))
async def mod(event):
    if event.fwd_from:
        return
    app = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, app) 
    await tap[0].click(event.chat_id)
    await event.delete()


@borg.on(admin_cmd(pattern="vid"))
async def mod(event):
    if event.fwd_from:
        return
    music =event.pattern_match.group(1)
    botusername = "@Vid"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, music)
    await tap[0].click(event.chat_id)
    await event.delete()

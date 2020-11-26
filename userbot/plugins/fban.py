# if You are reading this then Copy With Full Credits And After Reading you left the credits Then You are gonna be gay even the gay will disown you
# So Beter give credits 
# Fully Written By @rohithaditya 
# Special Thanks to Xditya he Was the one who tested the plugins
# This Plugin will Fban The User by this format "/fban 1234567890 or @username" 
# This Plugin Only Convey Msg to miss rosebot 
# -------- Keep credits else You beacome gay ----------- Wrote by rohithaditya for @Godhackerzuserbot --------------Corrected by @private_45-----------------------
# (C) @godhackerzuserbot
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
# ---------------------------------- Wrote by @Rohithaditya ------------------- For @godhackerzuserbot ---------Corrected by @Private_45----------------------------
@borg.on(admin_cmd(pattern="fban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    reason = event.pattern_match.group(1)
    victim = await event.get_reply_message()
    if not victim:
    	await event.edit("😈 Mention Someone To Ban 😈")
    else:
    	victim_id = victim.from_id
    	chat = "@MissRose_bot"
    	async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=609517172))
              await event.client.send_message(chat, "/fban {} {}".format(victim_id, reason))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("‼️ Unblock @MissRose_bot‼️ Master ")
              await event.client.send_message(event.chat_id, response.message)

# ---------------------------------- Wrote by @Rohithaditya ------------------------------------------ For @godhackerzuserbot ------------------------------------------
# Read First line before you beacome gay 
# Thanks to these guys :)
#  @private_45 
#  @xditya

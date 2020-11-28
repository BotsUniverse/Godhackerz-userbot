# if You are reading this then Copy With Full Credits And After Reading you left the credits Then You are gonna be gay even the gay will disown you
# So Beter give credits 
# Fully Written By @rohithaditya And @xditya 
# Special Thanks to Xditya he Was the one who tested the plugins And Rewrote for me
# This Plugin will Fban The User by this format "/fban 1234567890 or @username" 
# This Plugin will  Only Convey Msg to miss rosebot 
# -------- Keep credits else You beacome gay ----------- Wrote by rohithaditya for @Godhackerzuserbot ------------Edited by @Xditya for @Godhackerzuserbot--------
# (C) @godhackerzuserbot

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.util import admin_cmd
# -------- Keep credits else You beacome gay ----------- Wrote by rohithaditya for @Godhackerzuserbot ------------Edited By @Xditya For @Godhackerzuserbot---------
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
        if victim_id == "1207066133":
            await event.edit("LoL, you cant ban my Owner noob nibba")
            return
      async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=609517172))
              await event.client.send_message(chat, "/fban {} {}".format(victim_id, reason))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("‼️ Unblock @MissRose_bot‼️ Master")
              
  # -------- Keep credits else You beacome gay ----------- Wrote by rohithaditya for @Godhackerzuserbot -----------Edited By @Xditya For @Godhackerzuserbot-------
  # Must Ask Permisson Before kanging Or Cloning Else Go Commit Die or Beacome gay And You will b e beacoming our slave ------------------------------------------
  # Syntax = Fban The User by this format "/fban 1234567890 or @username" 

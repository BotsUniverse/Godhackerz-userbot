import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.util import admin_cmd

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
            await event.edit("LoL, you cant ban my master noob nibba")
            return
      async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=609517172))
              await event.client.send_message(chat, "/fban {} {}".format(victim_id, reason))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("‼️ Unblock @MissRose_bot‼") 

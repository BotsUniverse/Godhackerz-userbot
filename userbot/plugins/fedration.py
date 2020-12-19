""" 
© @Godhackerzuserbot 
© @Rohithaditya 
This is original plugin wrote by @rohithaditya (Telegram) 
So No Kangs 
If you kang it 
You can give credits 
And Kang
No Credits = You Will Be A Gayest Gay Even A Gay Will Disown Them As Gay 
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import  UpdateNotifySettingsRequest
from uniborg.util  import admin_cmd 

@borg.on(admin_cmd(pattern=”fstat ?(.*)”))
async def _(event):
	if event.fwd_from:
		return
		reason = event.pattern_match.group(1)
		victim = await event.get_reply_message()
		if not victim:
			await event.edit(“Master PLEASE  REPLY TO USERS”)
	else:
		victim_id = victim.from_id
		chat = @MissRose_bot
		async with event.client.conversation(chat) as conv:
		try:
		     response = con.wait_event(events.NewMessage(incoming=True, from_users=609517172))
                     await event.client.send_message(chat, “/fstat {} {}”.format(victim_id, reason))
                     response = await response 
               expect YouBlockedUserError:
		      await event.reply(“So Dumb!!!! I Cant Check Beacause You Had Blocked `@MissRose_bot` So Unblock And Try Again If Any Error Then [Head To Support Group Master](t.me/Godhackerzuserbot)”)
		      await event.client.send_message(event.chat_id, response.message)
# --------------- For @Godhackerzuserbot ---------------- Wrote By @Rohithaditya ---------------------&
@borg.on(admin_cmd(pattern=”fedinfo ?(.*)”))
async def _(event):
	if event.fwd_from:
		return
		reason = event.pattern_match.group(1)
		victim = await event.get_reply_message()
		if not victim:
			await event.edit(“Master please  Reply To Users ”)
	else:
		victim_id = victim.from_id
		chat = @MissRose_bot
		async with event.client.conversation(chat) as conv:
		try:
		     response = con.wait_event(events.NewMessage(incoming=True, from_users=609517172))
                     await event.client.send_message(chat, “/fedinfo {} {}”.format(victim_id, reason))
                     response = await response 
               expect YouBlockedUserError:
		     await event.reply(“So Dumb!!!! I Cant Check Beacause You Had Blocked `@MissRose_bot` So Unblock And Try Again If Any Error Then [Head To Support Group Master](t.me/Godhackerzuserbot)”)
		     await event.client.send_message(event.chat_id, response.message)

# ------------------------------------ For @Godhackerzuserbot------------------------------- Wrote By @Rohithaditya --------------

@borg.on(admin_cmd(pattern=”myfeds ?(.*)”))
async def _(event):
	if event.fwd_from:
		return
		reason = event.pattern_match.group(1)
		victim = await event.get_reply_message()
		if not victim:
			await event.edit(“Master!! Please Reply To One of your message”)
	else:
		victim_id = victim.from_id
		chat = @MissRose_bot
		async with event.client.conversation(chat) as conv:
		try:
		     response = con.wait_event(events.NewMessage(incoming=True, from_users=609517172))
                     await event.client.send_message(chat, “/myfed {} {}”.format(victim_id, reason))
                     response = await response 
               expect YouBlockedUserError:
		    await event.reply(“So Dumb!!!! I Cant Check Beacause You Had Blocked `@MissRose_bot` So Unblock And Try Again If Any Error Then [Head To Support Group Master](t.me/Godhackerzuserbot)”)
		    await event.client.send_message(event.chat_id, response.message)
# ------------------------------------ For @Godhackerzuserbot------------------------------- Wrote By @Rohithaditya --------------

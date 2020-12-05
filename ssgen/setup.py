from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("Please go-to my.telegram.org Login using your Telegram account Click on API Development Tools Create a new application, by entering the required details For Godhackerzuserbot")
print("")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    bot = client.send_message("me", client.session.save())
   bot.reply(
        "The above is the `STRING_SESSION` for your current session.\nJoin @Godhackerzuserbot For Support\n (c) ")
    print("")
    print("Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages.")
    print("")
    print("")
    print(client.session.save())

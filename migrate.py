from pyrogram import Client

apiID = 12345 # Edit this!
apiHash = "" string
oldChat = "" #chat name in string or chat id in interger
newChat = "" #chat name in string or chat id in interger
app = Client(
    "Migrate",
    api_id=,
    api_hash=)


with app:
    for message in app.iter_history(oldChat, reverse = True):
        app.forward_messages(
            chat_id=newChat,
            from_chat_id=message.chat.id,
            message_ids=message.message_id)

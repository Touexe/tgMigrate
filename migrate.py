from pyrogram import Client

apiID = 12345 # Edit this!
apiHash = "" string
oldChat = "" #chat name in string or chat id in interger
newChat = "" #chat name in string or chat id in interger
app = Client(
    "tgMigrate",
    api_id=,
    api_hash=)


with app:
    forwarded_count = 0
    for message in app.iter_history(oldChat, reverse = True):
        if message.service == True:
            continue   
        app.forward_messages(
            chat_id=newChat,
            from_chat_id=message.chat.id,
            message_ids=message.message_id)
        forwarded_count += 1
        print(f"[+] forward message {message.message_id} ({forwarded_count} forwarded)", end="\r")
    print(f"\n\n[+] Done! ")

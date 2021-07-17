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
    prev_media_group_id = ""
    for message in app.iter_history(oldChat, reverse = True):
        if message.service == True:
            continue
        
        media_group_id = message.media_group_id
        if media_group_id == prev_media_group_id:
            continue
            
        prev_media_group_id = message.media_group_id
        message_ids = [message.message_id]
        
        if media_group_id: #if it's not None
            message_group = app.get_media_group(oldChat, message.message_id)
            message_ids = [message.message_id for message in message_group]
        
        app.forward_messages(
            chat_id=newChat,
            from_chat_id=oldChat,
            message_ids= message_ids)
        forwarded_count += len(messsage_ids)
        print(f"[+] forward message {message.message_id} ({forwarded_count} forwarded)")

from pyrogram import Client

api_id = 2533573
api_hash = "43cb36a4ccc4113109953b6141ed3716"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "你好啊，Jordan")
from ..IMGClient import IMG
from pyrogram import filters
from pyrogram.types import Message
from ..workers.img_uploader import img_uploader


@IMG.on_message(filters.photo)
async def onPhotho(client, msg):
    file_path = await msg.download(file_name=f"downloads/{msg.chat.id}/")
    see = await img_uploader(file_path=file_path)
    print(see['data']['url'])

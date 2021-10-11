from ..IMGClient import IMG
from pyrogram import filters


@IMG.on_message(filters.photo)
async def onPhotho(_, msg):
    await msg.download(file_name="hi.jpg")

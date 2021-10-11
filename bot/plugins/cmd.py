from bot.IMGClient import IMG
from pyrogram import filters


@IMG.on_message(filters.command("start"))
async def onStart(_, msg):
    await msg.reply("Hello")

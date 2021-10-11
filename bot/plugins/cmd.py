from bot.IMGClient import IMG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

_keyboard = [
    [
        InlineKeyboardButton("Developer",
                             url="https://github.com/AbhijithNT/"),
        InlineKeyboardButton("Contact", url='tg://user?id=1087968824')
    ],
    [
        InlineKeyboardButton(  # Opens the inline interface
            "Source code",
            url="https://github.com/AbhijithNT/TGImageHosting"),
        InlineKeyboardButton(  # Opens the inline interface in the current chat
            "Suggestions and Issues",
            url="https://github.com/AbhijithNT/TGImageHosting/issues/new")
    ]
]


@IMG.on_message(filters.command("start"))
async def onStart(_, msg):
    await msg.reply_text(
        f"**Hi! [{msg.chat.first_name}](tg://user?id={msg.chat.id}),\nThis is a simple bot that can be used to upload images to a third-party cloud (image hosting). Currently, only the** ``imgbb.com`` **website supports the bot. I Will do future updates**",
        reply_markup=InlineKeyboardMarkup(_keyboard))

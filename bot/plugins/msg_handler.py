from ..IMGClient import IMG
from pyrogram import filters
from ..workers.img_uploader import img_uploader
from ..workers.img_remove import deleteME


@IMG.on_message(filters.photo)
async def onPhotho(client, msg):
    client_msg = await client.send_message(chat_id=msg.chat.id,
                                           text="Downloading...",
                                           reply_to_message_id=msg.message_id)
    file_path = await msg.download(file_name=f"downloads/{msg.chat.id}/")
    responce = await img_uploader(file_path=file_path, msg=client_msg)
    if (responce is None):
        return
    title = responce['data']['title']
    await client.edit_message_text(
        chat_id=msg.chat.id,
        message_id=client_msg.message_id,
        text=
        f"**Name: {title}\nDirect URL: [{title}]({responce['data']['url']})**",
        parse_mode="markdown",
    )
    await deleteME(file_path=file_path)


@IMG.on_message(filters.document)
async def onDocument(client, msg):
    mime_type = [
        'application/pdf', 'image/bmp', 'image/gif', 'image/tiff',
        'image/webp', 'image/jpeg', 'image/png'
    ]
    if (msg.document.mime_type not in mime_type):
        msg.reply('Sorry, this format is not supported 🙂')
    else:
        client_msg = await client.send_message(
            chat_id=msg.chat.id,
            text="Downloading...",
            reply_to_message_id=msg.message_id)
        file_path = await msg.download(file_name=f"downloads/{msg.chat.id}/")
        responce = await img_uploader(file_path=file_path, msg=client_msg)
        if (responce is None):
            return
        title = responce['data']['title']
        await client.edit_message_text(
            chat_id=msg.chat.id,
            message_id=client_msg.message_id,
            text=
            f"**Name: {title}\nDirect URL: [{title}]({responce['data']['url']})**",
            parse_mode="markdown",
        )
        await deleteME(file_path=file_path)
from pyrogram import Client
from sample_cofig import (API_ID, API_HASH, BOT_TOKEN)


class IMG(Client):
    def __init__(self):
        super().__init__("session_name",
                         api_id=API_ID,
                         api_hash=API_HASH,
                         bot_token=BOT_TOKEN,
                         plugins={"root": "bot/plugins"})

    async def start(self):
        await super().start()

    async def stop(self, *args):
        await super().stop()

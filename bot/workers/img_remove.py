import os


async def deleteME(file_path: str):
    try:
        os.remove(file_path)
    except OSError as e:
        print(e)
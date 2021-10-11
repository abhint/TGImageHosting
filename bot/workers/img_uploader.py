import requests


async def img_uploader(file_path: str):
    _params = {
        'key': '9076a9d6de80de9fc13ea32268c664ea',
    }

    _files = {'image': open(file_path, 'rb')}

    response = requests.post('https://api.imgbb.com/1/upload',
                             params=_params,
                             files=_files).json()
    return response
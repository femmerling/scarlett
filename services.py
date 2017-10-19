from os import environ
import requests
from sanic import response

async def get_image_content(image_url):
    full_url = "http://{}".format(image_url)
    try:
        image = requests.get(full_url)
        if image.status_code > 399:
            image = requests.get(environ.get('SCARLETT_DEFAULT_IMG'))
    except:
        image = requests.get(environ.get('SCARLETT_DEFAULT_IMG'))
    return image.content


def get_mimetype(image_url):
    mimetypes = {
        "jpg":"image/jpeg",
        "jpeg":"image/jpeg",
        "gif":"image.gif",
        "png":"image.png"}

    extension = image_url.split(".")[-1].lower()
    return mimetypes[extension]

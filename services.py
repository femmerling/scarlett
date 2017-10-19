from os import environ
import requests
from sanic import response
from datetime import datetime
from datetime import timedelta
from email.utils import format_datetime

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

def set_expiry_headers():
    current = datetime.utcnow()
    expiry_time = current + timedelta(days=30)
    max_age = 3600*720
    return {
        'Expires':format_datetime(expiry_time),
        'Cache-Control':'public,max-age={}'.format(max_age)
    }

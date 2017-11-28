from datetime import datetime
from datetime import timedelta
from email.utils import format_datetime
from os import environ
from errors import BadRequestError

import requests


MIMETYPE_JPEG = 'image/jpeg'
MIMETYPE_GIF = 'image/gif'
MIMETYPE_PNG = 'image/png'
MIMETYPE_BMP = 'image/bmp'
MIMETYPE_ICO = 'image/x-icon'
MIMETYPE_TIF = 'image/tiff'
MIMETYPE_WEBP = 'image/webp'

EXT_JPEG = [
    'jpg',
    'jpeg',
    'jpe',
    'jfif'
]
EXT_GIF = [
    'gif'
]
EXT_PNG = [
    'x-png',
    'png'
]
EXT_BMP = [
    'bm',
    'bmp'
]
EXT_ICO = [
    'ico'
]
EXT_TIF = [
    'tif',
    'tiff'
]
EXT_WEBP = [
    'webp'
]

DEFAULT_MIMETYPE = 'image/*'

MIMETYPE_EXT_MAP = {
    MIMETYPE_JPEG: EXT_JPEG,
    MIMETYPE_GIF: EXT_GIF,
    MIMETYPE_PNG: EXT_PNG,
    MIMETYPE_BMP: EXT_BMP,
    MIMETYPE_ICO: EXT_ICO,
    MIMETYPE_TIF: EXT_TIF,
    MIMETYPE_WEBP: EXT_WEBP
}

def get_version():
    with open('version.txt', "r") as ver:
        return ver.readline().replace('\n','')

async def get_image_content(image_url):
    full_url = "http://{}".format(image_url)
    user_agent = "Scarlett by Prismapp {}".format(get_version())
    try:
        headers = {
            "User-Agent":user_agent}
        image = requests.get(full_url, headers=headers)
        if image.status_code > 399:
            image = requests.get(environ.get('SCARLETT_DEFAULT_IMG'))
    except:
        image = requests.get(environ.get('SCARLETT_DEFAULT_IMG'))
    return image.content


def get_image_extension(image_url):
    extension = image_url.split('.')
    if len(extension) == 0:
        raise BadRequestError('No valid extensions detected')

    extension = extension[-1].lower()

    return extension


def get_mimetype(image_url):
    extension = get_image_extension(image_url=image_url)

    mimetype = DEFAULT_MIMETYPE
    for (mtype, extensions) in MIMETYPE_EXT_MAP.items():
        if extension in extensions:
            mimetype = mtype

    return mimetype


def set_expiry_headers():
    current = datetime.utcnow()
    expiry_time = current + timedelta(days=30)
    max_age = 3600 * 720
    return {
        'Expires': format_datetime(expiry_time),
        'Cache-Control': 'public,max-age={}'.format(max_age)
    }

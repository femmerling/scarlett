from os import environ
import requests
from sanic import response

async def get_image_content(request):
    image_url = request.args.get('url')
    image = requests.get(image_url)
    if image.status_code == 404:
        image = requests.get(environ.get('SCARLETT_DEFAULT_IMG'))
    return image.content

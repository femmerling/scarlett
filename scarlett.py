from sanic import Sanic
from sanic import response as sanic_response
from config.env import set_default_config

set_default_config()

from services import get_image_content
from services import get_mimetype
from services import set_expiry_headers


def create_app():
    app = Sanic(__name__)

    @app.route('/<image_url:path>')
    async def index(request, image_url):
        content_type = get_mimetype(image_url=image_url)
        headers = set_expiry_headers()

        async def get_image(response):
            content = await get_image_content(image_url)
            response.write(content)

        return sanic_response.stream(
            get_image,
            content_type=content_type,
            headers=headers)

    return app

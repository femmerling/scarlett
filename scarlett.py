from sanic import Sanic
from sanic import response
from config.env import set_default_config

set_default_config()

from services import get_image_content

def create_app():
    app = Sanic(__name__)

    @app.route('/')
    async def index(request):
        async def get_image(response):
            content = await get_image_content(request)
            response.write(content)
        return response.stream(get_image, content_type='image/jpg')

    return app




from os import environ
from app import create_app

app = create_app()

if __name__ == "__main__":
    debug = True if environ.get('SCARLETT_DEBUG') == '1' else False
    app.run(
        host=environ.get('SCARLETT_HOST'),
        port=int(environ.get('SCARLETT_PORT')),
        debug=debug)

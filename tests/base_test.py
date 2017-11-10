from scarlett import create_app
import unittest


JPG_TEST_URL = ''
GIF_TEST_URL = 'media.giphy.com/media/IL4iTvQH0MjS/giphy.gif'


class BaseTest(unittest.TestCase):

    app = None

    def setUp(self):
        self.app = create_app().test_client

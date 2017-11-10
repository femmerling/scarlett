from tests.base_test import BaseTest, GIF_TEST_URL
from nose.tools import eq_


class RequestTest(BaseTest):

    def test_get_image_succes(self):
        request, response = self.app.get('/%s' % GIF_TEST_URL)

        eq_(response.status, 200,
            msg='Valid request should return 200')

    def test_get_image_failed_returns_default_image(self):
        request, response = self.app.get('/%s' % GIF_TEST_URL)

        eq_(response.status, 200,
            msg='Valid request should return 200')

    def test_invalid_url_returns_default_image(self):
        request, response = self.app.get('/invalid.url/image.jpeg')

        eq_(response.status, 200,
            msg='Valid request should return 200')

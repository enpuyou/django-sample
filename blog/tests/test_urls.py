from django.urls import reverse, resolve


class TestUrls:

    def test_detail_url(self):
        path = reverse('blog-home', kwargs=None)
        assert resolve(path).view_name == 'blog-home'

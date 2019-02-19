from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from blog.views import home
from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db

class TestViews:

    def test_product_detail_authenticated(self):
        mixer.blend('blog.Post')
        path = reverse('blog-home', kwargs=None)
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

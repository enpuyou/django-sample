from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db

class TestModels:

    def test_post_is_in_stock(self):
        post = mixer.blend('blog.Post', quantity=1)
        assert post.is_in_stock == True

    def test_model(self):
        post = mixer.blend('blog.Post')
        assert post.pk == 1

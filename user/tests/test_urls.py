from django.urls import reverse, resolve


class TestUrls:

    def test_user_viewset(self):
        path = reverse('user-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'user-detail'
        path = reverse('user-list')
        assert resolve(path).view_name == 'user-list'

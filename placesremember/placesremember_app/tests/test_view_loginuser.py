from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse


from placesremember_app.utils import menu
from placesremember_app.views import LoginUser


class LoginUserViewTest(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "testuser",
            "password": "testpswd",
        }
        self.factory = RequestFactory()
        self.user = User.objects.create_user(**self.credentials)

    def test_get_context_data(self):
        request = self.factory.get(reverse("login"))
        request.user = self.user
        self.view = LoginUser.as_view()
        response = self.view(request)
        self.assertEqual(response.context_data["menu"], menu)
        self.assertEqual(response.context_data["title"], "Sign In")

    def test_login(self):
        response = self.client.post(reverse("login"), self.credentials, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)

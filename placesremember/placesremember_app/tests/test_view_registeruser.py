from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from placesremember_app.forms import RegisterUserForm
from placesremember_app.utils import menu
from placesremember_app.views import RegisterUser


class RegisterUserViewTest(TestCase):
    def setUp(self):
        self.form_data = {
            "username": "testuser",
            "password1": "testpswd",
            "password2": "testpswd",
        }
        self.factory = RequestFactory()
        self.client = Client()
        self.form = RegisterUserForm(data=self.form_data)

    def test_get_context_data(self):
        request = self.factory.get(reverse("login"))
        self.view = RegisterUser.as_view()
        response = self.view(request)
        self.assertEqual(response.context_data["menu"], menu)
        self.assertEqual(response.context_data["title"], "Sign Up")

    def test_form_valid(self):
        self.assertTrue(self.form.is_valid())

    def test_sign_up(self):
        response = self.client.post(reverse("register"), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username="testuser").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)

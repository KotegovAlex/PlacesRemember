from django.test import Client, TestCase
from django.urls import reverse


class LogutUserViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logout_user(self):
        self.client.login(username="testuser", password="testpswd")
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("home"))

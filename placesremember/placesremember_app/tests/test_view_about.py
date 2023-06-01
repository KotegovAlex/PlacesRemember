from django.test import Client, TestCase
from django.urls import reverse

from placesremember_app.views import menu


class AboutViewTest(TestCase):
    def test_context(self):
        client = Client()
        response = client.get(reverse("about"))
        self.assertEqual(response.context["menu"], menu)

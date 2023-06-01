from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse

from placesremember_app.forms import AddPlaceForm
from placesremember_app.utils import menu
from placesremember_app.views import AddPlace


class AddPlaceViewTest(TestCase):
    def setUp(self):
        self.form_data = {
            "title": "testplace",
            "content": "testcontent",
        }
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser_1", password="testpswd1",
        )

    def test_get_context_data(self):
        request = self.factory.get(reverse("add_place"))
        request.user = self.user
        self.view = AddPlace.as_view()
        response = self.view(request)
        self.assertEqual(response.context_data["menu"], menu)

    def test_form_valid(self):
        form = AddPlaceForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_valid_on_create_view(self):
        request = self.factory.post(reverse("add_place"), data=self.form_data)
        request.user = self.user
        response = AddPlace.as_view()(request)
        self.assertTrue(response)

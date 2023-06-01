from django.contrib.auth.models import User
from django.test import TestCase

from placesremember_app.forms import AddPlaceForm


class AddPlaceFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpswd")

    def test_form_validation_and_save(self):
        form_data = {
            "title": "Test Place",
            "content": "Test content",
        }
        form = AddPlaceForm(data=form_data)
        self.assertTrue(form.is_valid())

        place = form.save(commit=False)
        place.user_id = self.user
        self.assertEqual(place.title, "Test Place")
        self.assertEqual(place.content, "Test content")
        self.assertEqual(place.user_id, self.user)

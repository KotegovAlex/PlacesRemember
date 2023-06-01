from django.contrib.auth.models import User
from django.test import TestCase

from placesremember_app.models import Place


class PlaceModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            username="Test user",
            password="1",
        )
        cls.place = Place.objects.create(
            title="Test place title",
            content="Test content",
            user_id=PlaceModelTest.user,
        )

    def test_title_label(self):
        """verbose_name поля title совпадает с ожидаемым"""
        place = PlaceModelTest.place
        verbose = place._meta.get_field("title").verbose_name
        self.assertEqual(verbose, "Place Title")

    def test_content_label(self):
        """verbose_name поля content совпадает с ожидаемым"""
        place = PlaceModelTest.place
        verbose = place._meta.get_field("content").verbose_name
        self.assertEqual(verbose, "Comment")

    def test_str(self):
        """method __str__ test"""
        place = PlaceModelTest.place
        self.assertEqual(place.__str__(), "Test place title")

    def test_get_absolute_url(self):
        """method get_absolute_url test"""
        place = PlaceModelTest.place
        self.assertEqual(place.get_absolute_url(), "/place/1/")

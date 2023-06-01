from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse

from placesremember_app.models import Place
from placesremember_app.utils import menu
from placesremember_app.views import ShowPlace


class ShowPlaceViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="testuser", password="testpswd")
        self.place = Place.objects.create(
            title="testuser_1",
            content="testpswd1",
            user_id=self.user,
        )

    def test_get_context_data(self):
        request = self.factory.get(reverse("place", kwargs={"place_id": self.place.pk}))
        response = ShowPlace.as_view()(request, place_id=self.place.pk)
        context = response.context_data
        self.assertEqual(context["menu"], menu)

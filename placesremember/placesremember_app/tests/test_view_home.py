from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from placesremember_app.models import Place
from placesremember_app.views import Home


class HomeViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user_1 = User.objects.create_user(
            username="testuser_1", password="testpswd1"
        )
        self.user_2 = User.objects.create_user(
            username="testuser_2", password="testpswd2"
        )
        self.place_1 = Place.objects.create(
            title="Test place_1 title",
            content="Place_1 test content",
            user_id=self.user_1,
        )
        self.place_2 = Place.objects.create(
            title="Test place_2 title",
            content="Place_2 test content",
            user_id=self.user_2,
        )

    def test_get_queryset(self):
        request = self.factory.get(reverse("home"))
        request.user = self.user_1
        view = Home.as_view()
        response = view(request)
        self.assertQuerysetEqual(
            response.context_data["object_list"],
            Place.objects.filter(user_id=self.user_1.pk),
        )

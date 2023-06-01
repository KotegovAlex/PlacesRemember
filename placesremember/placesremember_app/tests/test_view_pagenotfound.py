from django.test import Client, TestCase


class PageNotFoundViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_not_found(self):
        response = self.client.get("/non-existent-url/")
        self.assertContains(response, "<h1>Page Not Found</h1>", status_code=404)

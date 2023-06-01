from django.test import TestCase

from placesremember_app.utils import DataMixin, menu


class DataMixinTest(TestCase):
    def test_get_user_context(self):
        mixin = DataMixin()
        context = mixin.get_user_context()
        self.assertEqual(context["menu"], menu)

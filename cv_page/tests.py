from django.test import TestCase
from django.urls import resolve
from cv_page.views import cv


class HomePageTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        found = resolve('/cv.html')
        self.assertEqual(found.func, cv)

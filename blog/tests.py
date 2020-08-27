from django.test import TestCase
from django.urls import resolve
from blog.views import cv


class CVTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        found = resolve('/')
        self.assertEqual(found.func, cv)

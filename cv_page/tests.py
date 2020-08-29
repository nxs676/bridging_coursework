from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from cv_page.views import cv


class CVPageTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        found = resolve('/cv.html')
        self.assertEqual(found.func, cv)

    def test_cv_returns_correct_html(self):
        response = self.client.get('/cv.html')
        self.assertTemplateUsed(response, 'cv.html')

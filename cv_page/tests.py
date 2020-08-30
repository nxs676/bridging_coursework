from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from cv_page.models import CV
from cv_page.views import cv_url


class CVPageTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        found = resolve('cv_page/cv.html')
        self.assertEqual(found.func, cv_url)

    def test_cv_returns_correct_html(self):
        response = self.client.get('cv_page/cv.html')
        self.assertTemplateUsed(response, 'cv.html')


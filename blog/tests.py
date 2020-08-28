from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from blog.views import cv


class CVTest(TestCase):

    def test_root_url_resolves_to_cv_view(self):
        found = resolve('/cv.html')
        self.assertEqual(found.func, cv)

    def test_cv_returns_correct_html(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>CV</title>', html)
        self.assertTrue(html.endswith('</html>'))

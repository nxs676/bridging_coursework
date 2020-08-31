from django.test import TestCase


class CVPageTest(TestCase):

    def test_cv_returns_correct_html(self):
        response = self.client.get('/cv/7/edit')
        self.assertTemplateUsed(response, 'cv_page/cv.html')

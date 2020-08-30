from django.test import TestCase
from cv_page.models import CV


class CVModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CV.objects.create(name='name', address='address', phone='123456789', email='a@email.com', summary='summary',
                          skills='skills', education='education', jobs='jobs')

    def test_name_max_length(self):
        cv = CV.objects.get(id=1)
        max_length = cv._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_address_max_length(self):
        cv = CV.objects.get(id=1)
        max_length = cv._meta.get_field('address').max_length
        self.assertEquals(max_length, 300)

    def test_phone_max_length(self):
        cv = CV.objects.get(id=1)
        max_length = cv._meta.get_field('phone').max_length
        self.assertEquals(max_length, 50)

    def test_string_representation(self):
        self.fail("TODO Test incomplete")



from django.test import TestCase
from cv_page.models import CV


class CVModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CV.objects.create(name='name', address='address', phone='123456789', email='a@email.com',
                          summary='summary',
                          skills='skills', education='education', jobs='jobs')

    def test_model_creation(self):
        cv = CV.objects.create(name='name', address='address')
        self.assertTrue(isinstance(cv, CV))
        self.assertEqual(cv.__str__(), cv.name)


    def test_name_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_address_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('address').max_length
        self.assertEquals(max_length, 300)

    def test_phone_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('phone').max_length
        self.assertEquals(max_length, 50)

    def test_summary_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('summary').max_length
        self.assertEquals(max_length, 2000)

    def test_skills_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('skills').max_length
        self.assertEquals(max_length, 2000)

    def test_education_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('education').max_length
        self.assertEquals(max_length, 2000)

    def test_jobs_max_length(self):
        cv = CV.objects.get()
        max_length = cv._meta.get_field('jobs').max_length
        self.assertEquals(max_length, 2000)

    def test_string_representation(self):
        self.fail("TODO Test incomplete")

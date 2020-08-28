from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_CV_and_edit_later(self):
        self.browser.get('http://localhost:8000/cv.html')
        self.assertIn('/cv.html', self.browser.current_url)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

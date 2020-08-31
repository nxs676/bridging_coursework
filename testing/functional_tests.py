from selenium import webdriver
import unittest


class NikolTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_CV_and_edit_(self):
        self.browser.get('http://localhost:8000/cv.html')
        self.assertIn('cv.html', self.browser.current_url)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

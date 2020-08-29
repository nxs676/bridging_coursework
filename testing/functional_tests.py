import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_CV_and_edit_(self):
        self.browser.get('http://localhost:8000/cv.html')
        self.assertIn('/cv.html', self.browser.current_url)

        # header_text = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('CV', header_text)
        #
        # inputbox = self.browser.find_element_by_id('id_new_info')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Update information'
        # )
        # inputbox.send_keys('New information')
        #
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        #
        # table = self.browser.find_element_by_id('id_info_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == 'Employment' for row in rows),
        #     "New employment item did not appear in table"
        # )
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

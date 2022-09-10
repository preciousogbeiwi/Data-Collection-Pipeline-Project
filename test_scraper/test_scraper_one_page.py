from scrape_data.scrape_one_page import Scraper_project
import unittest

'''
Testing the extracting_data script
'''

class Scraper_projectTestCase(unittest.TestCase):
    # Initialize the scenario for your test
    def setUp(self):
        self.b = Scraper_project()
    
    def test_accept_cookies(self):
        expected_value = "Accept All Cookies"
        actual_value = self.b.accept_cookies().text
        self.assertEqual(expected_value, actual_value)

    def test_bestsellers(self):
        expected_value = "SEE MORE"
        actual_value = self.b.bestsellers().text
        self.assertEqual(expected_value, actual_value)

    #def test_extract_data(self):
    #    expected_value = "Robert Galbraith"
    #    actual_value = self.b.extract_data()['Author'][0]
    #    self.assertEqual(expected_value, actual_value)

    # Finish 
    #def tearDown(self):
    #    del self.driver.close()

# Driver code
if __name__ == "__main__":
    unittest.main()
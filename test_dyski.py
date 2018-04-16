from selenium import webdriver
import unittest
import logging
# import time

from CeneoPages.ceneo_pages import ChooseCategory


class DyskiClick(unittest.TestCase):

    """

    This class tests ceneo login and click on dyski link
    It also clicks komputery & podzespoly komputerowe links

    """

    def setUp(self):

        """
        This function is used to make initial setup for this taest case.
        """

        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Lukasz\Desktop\Programowanie\geckodriver.exe')
        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename='test.log', level=logging.INFO, format=logging_format)
        self.log = logging.getLogger(__name__)

    def test_ceneo_dyski(self):

        """

        This page is to test login ceneo page

        """

        driver = self.driver
        ceneo_login = ChooseCategory(driver, root_uri=None)
        ceneo_login.get('https://ceneo.pl')
        self.log.info('LOGGED URL: %s %s' % (driver.current_url, self._testMethodName))
        page = ceneo_login.return_ceneo_page()

        # This validates ceneo.pl login
        title_ceneo = "Ceneo - porównanie cen, sklepy, perfumy, agd, rtv, komputery"
        self.assertEqual(page.get_page_title(), title_ceneo)

        # This calls function to click on komputery link
        komputery_page = page.choose_komputery()
        self.log.info('LOGGED URL: %s', driver.current_url)

        # This validates ceneo.pl/komputery login
        title_komputery = "Komputery - Ceneo.pl"
        self.assertEqual(komputery_page.get_komputery_title(), title_komputery)

        # This calls function to click on podzespoły komputerowe link and
        # returns podzespoly_komputerowe object
        podzespoly_komputerowe_page = komputery_page.choose_podzespoly_komputerowe()
        self.log.info('LOGGED URL: %s', driver.current_url)

        # This validates ceneo.pl/podzespoly_komputerowe
        self.assertEqual(podzespoly_komputerowe_page.get_podzespoly_title(),
                         'Podzespoły komputerowe, części komputerowe - Ceneo.pl')

        # This makes click on dyski link
        dyski_page = podzespoly_komputerowe_page.choose_dyski()
        self.log.info('LOGGED URL: %s', driver.current_url)

        # Disk page validation
        self.assertEqual(dyski_page.get_dyski_title(), 'Dyski komputerowe - Ceneo.pl')


    def tearDown(self):

        self.driver.get_screenshot_as_file("screen_{}.png".format(self._testMethodName))
        self.driver.close()
        pass

if __name__ == '__main__':

    unittest.main()
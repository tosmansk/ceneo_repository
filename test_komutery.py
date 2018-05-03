# -*- coding: utf8 -*-

from selenium import webdriver
import unittest
import logging
import time
from ceneo_pages import ChooseCategory
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import configparser

class KomputeryClick(unittest.TestCase):

    """

    This class tests ceneo login and click on komputery link

    """

    def setUp(self):

        """
        This function is used to make initial setup for this taest case.
        """
        """
        This reads IP config from the file:
        with open('remote_server.cfg', 'r') as config:
            uri = config.readline()
        """

        config = configparser.ConfigParser()
        config.read('ipconfig.ini')
        uri = config['Selenium']['url']

        self.driver = webdriver.Remote(command_executor=uri, desired_capabilities=DesiredCapabilities.FIREFOX)
        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename='test.log', level=logging.INFO, format=logging_format)
        self.log = logging.getLogger(__name__)

    def test_ceneo_komputery(self):

        """

        This page is to test login ceneo page

        """

        driver = self.driver
        ceneo_login = ChooseCategory(driver, root_uri=None)
        ceneo_login.get('https://ceneo.pl')
        self.log.info('LOGGED URL: %s', driver.current_url)
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

    def tearDown(self):
        time.sleep(2)
        self.driver.get_screenshot_as_file("screen_{}.png".format(self._testMethodName))
        self.driver.close()



if __name__ == '__main__':

    unittest.main()

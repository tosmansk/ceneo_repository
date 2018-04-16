from page_objects import PageObject, PageElement
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait

class ChooseCategory(PageObject):

    """
    This class will log in ceneo and will choose category to search on https://www.ceneo.pl/
    The categories will be added to this class. Initially it will be computers category

    komputery: <a class="cat-link category-icon-43" href="/Komputery">Komputery</a>
    xpath = "//a[@href="/Komputery"]
    css = .cat-link.category-icon-43

    """

    komputery_element = PageElement(xpath="//a[@href='/Komputery']")


    def return_ceneo_page(self):
        return self

    def get_page_title(self):

        """

        This function gives expected page title after login

        """
        time.sleep(2)
        return self.w.title

    def choose_komputery(self):

        """

        This function makes click action on komputery link

        """

        ac = ActionChains(self.w)
        ac.move_to_element(self.komputery_element)
        action = ac.click(self.komputery_element)
        action.perform()
        time.sleep(2)

        return KomputeryPage(self.w, root_uri='https://www.ceneo.pl/Komputery')


class KomputeryPage(PageObject):

    """

    This class will resolved some elemets and action of Komputery Page
    Return title

    """

    podzespoly_komputerowe_element = PageElement(css="a.js_categories-link[href='/Podzespoly_komputerowe']")
    button_element = PageElement(css="button.disable-sticky-header")

    def get_komputery_title(self):

        """

        This function returns page title
        :return: str Komputery - Ceneo pl

        """
        time.sleep(2)
        return self.w.title

    def choose_podzespoly_komputerowe(self):

        """

        This function makes click action on podzespoły komputerowe link

        """

        ac = ActionChains(self.w)
        self.podzespoly_komputerowe_element.location_once_scrolled_into_view

        def sprawdz_button(action):

            if self.button_element.is_displayed():
                action.click(self.button_element)
                action.perform()
            else:
                WebDriverWait(self.w, 2).until(self.button_element.is_displayed())
                action.click(self.button_element)
                action.perform()

        sprawdz_button(ac)
        self.podzespoly_komputerowe_element.click()
        time.sleep(2)

        return PodzespolyKomputerowe(self.w, root_uri='https://www.ceneo.pl/Podzespoly_komputerowe')


class PodzespolyKomputerowe(PageObject):

    """

    This class will resolved some elemets and action of Podzespoły Komputerowe Page
    Return title

    """

    dyski_element = PageElement(css="a.js_categories-link[href='/Dyski']")

    def get_podzespoly_title(self):

        """

        This function returns page title
        :return: str 'Podzespoły komputerowe, części komputerowe - Ceneo.pl'

        """
        time.sleep(2)
        return self.w.title

    def choose_dyski(self):

        """

        This function makes click action on komputery link

        """

        ac = ActionChains(self.w)
        action = ac.click(self.dyski_element)
        action.perform()
        time.sleep(2)

        return Dyski(self.w, root_uri='https://www.ceneo.pl/Dyski')


class Dyski(PageObject):

    """
    This class will resolve elements on page "Dyski"
    """

    def get_dyski_title(self):

        """

        This function returns page title
        :return: str 'Dyski komputerowe - Ceneo.pl'

        """

        time.sleep(3)
        return self.w.title
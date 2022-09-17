from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.header import Header


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)
        self.header = Header(self.driver)
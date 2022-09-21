from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.header import Header
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)
        self.header = Header(self.driver)
        self.product_page = ProductPage(self.driver)
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.bestsellers_page = BestsellersPage(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)
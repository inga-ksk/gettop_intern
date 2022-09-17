from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    CART_ICON = (By.CSS_SELECTOR, 'ul.header-nav span.cart-icon')
    CART_ICON_COUNT = (By.CSS_SELECTOR, 'ul.header-nav span.cart-icon strong')

    def cart_icon_count(self):
        self.verify_element_text("1", *self.CART_ICON_COUNT)
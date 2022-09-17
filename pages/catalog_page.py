from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains

class CatalogPage(Page):

    QUICK_VIEW_LINK = (By.CSS_SELECTOR, "a.quick-view")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.product-small img.attachment-woocommerce_thumbnail")
    QUICK_VIEW_CONTAINER = (By.CSS_SELECTOR, "div.product-quick-view-container")
    QUICK_VIEW_CLOSE_X = (By.CSS_SELECTOR, 'button.mfp-close')
    PRODUCT_CATALOG_PAGE_COUNT = (By.CSS_SELECTOR, 'p.woocommerce-result-count')
    ADD_PRODUCT_TO_CART_QUICK_VIEW = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, 'div.message-container')
    CATALOG_PAGE_2 = (By.CSS_SELECTOR, 'ul.page-numbers li:nth-child(2)')
    CATALOG_RIGHT_ARROW = (By.CSS_SELECTOR, 'i.icon-angle-right')
    CATALOG_LEFT_ARROW = (By.CSS_SELECTOR, 'i.icon-angle-left')


    def hover_product_image(self):
        product_thumbnail = self.find_element(*self.PRODUCT_IMAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(product_thumbnail)
        actions.perform()

    def quick_view_click(self):
        self.wait_for_element_click(*self.QUICK_VIEW_LINK)

    def quick_view_window_presence(self):
        self.wait_for_element_appear(*self.QUICK_VIEW_CONTAINER)

    def quick_view_close(self):
        self.wait_for_element_click(*self.QUICK_VIEW_CLOSE_X)

    def catalog_page_1_open(self):
        self.verify_partial_text("Showing 1–12 of ", *self.PRODUCT_CATALOG_PAGE_COUNT)

    def catalog_page_2_open(self):
        self.verify_partial_text("Showing 13–24 of ", *self.PRODUCT_CATALOG_PAGE_COUNT)

    def add_to_cart_click(self):
        self.wait_for_element_click(*self.ADD_PRODUCT_TO_CART_QUICK_VIEW)

    def catalog_page_2_click(self):
        self.wait_for_element_click(*self.CATALOG_PAGE_2)

    def catalog_switch_right_arrow_click(self):
        self.wait_for_element_click(*self.CATALOG_RIGHT_ARROW)

    def catalog_switch_left_arrow_click(self):
        self.wait_for_element_click(*self.CATALOG_LEFT_ARROW)
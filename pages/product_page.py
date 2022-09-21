from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

class ProductPage(Page):

    REVIEW_TAB = (By.ID, 'tab-title-reviews')
    RATING_4_STAR = (By.CSS_SELECTOR, 'a.star-4')
    REVIEW_TEXT_FIELD = (By.ID, 'comment')
    NAME_FIELD = (By.ID, 'author')
    EMAIL_FIELD = (By.ID, 'email')
    SUBMIT_BUTTON = (By.ID, 'submit')
    REVIEW_APPROVAL_LABEL = (By.CSS_SELECTOR, 'em.woocommerce-review__awaiting-approval')

    def review_tab_click(self):
        self.wait_for_element_click(*self.REVIEW_TAB)

    def choose_4_star(self):
        self.click(*self.RATING_4_STAR)

    def input_review_text(self):
        def current_time():
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time = current_time()
        self.input_text(f"New comment + {time}", *self.REVIEW_TEXT_FIELD)

    def input_name_and_email(self):
        self.input_text("Test Name", *self.NAME_FIELD)
        self.input_text('daprauttobeudde-8124@yopmail.com', *self.EMAIL_FIELD)

    def submit_click(self):
        self.click(*self.SUBMIT_BUTTON)

    def verify_review_waiting_approval_status(self):
        self.verify_element_text('Your review is awaiting approval', *self.REVIEW_APPROVAL_LABEL)
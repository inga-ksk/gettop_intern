from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url()

    def open_url(self, end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')
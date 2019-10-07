# results
from selenium.webdriver.common.by import By
from pypom import Page

class GoogleResults(Page):
    _result_divs = (By.CLASS_NAME, 'rc')
    _search_field = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    @property
    def search_field(self):
        return self.browser.find_element(*self._search_field)

    def result_div_count(self):
        result_divs = self.browser.find_elements(*self._result_divs)
        return len(result_divs)

    def search_input_value(self, search_field):
        return search_field.get_attribute('value')

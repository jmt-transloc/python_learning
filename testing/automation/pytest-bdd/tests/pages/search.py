# search
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pypom import Page

class GoogleSearch(Page):
    test_var = 'Google Search'
    _url = 'https://www.google.com'
    _search_input = (By.NAME, 'q')
    _search_button = (By.CSS_SELECTOR, f'[aria-label="{test_var}"]')

    #
    # @param browser - A reference to the web driver browser instance
    #
    def __init__(self, browser):
        self.browser = browser

    # 
    # Page Methods
    # 
    def load(self):
        self.browser.get(self._url)

    def get_title(self):
        title = self.browser.title
        return title

    #
    # @param phrase - A search phrase (text or int)
    #
    def search(self, phrase):
        self.browser.find_element(*self._search_button)
        search_input = self.browser.find_element(*self._search_input)
        search_input.send_keys(phrase + Keys.RETURN)

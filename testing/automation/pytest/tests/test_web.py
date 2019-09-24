# test_web
import pytest
import json

from pages.search import GoogleSearchPage
from pages.results import GoogleResultsPage

from selenium.webdriver import Chrome

@pytest.fixture(scope='session')
def config():
    with open('tests/config.json') as config_file:
        data = json.load(config_file)
    return data

#
# Create a browser fixture. Fixtures are called once per test function
# unless otherwise specified.
#
@pytest.fixture
def browser(config):
    if config['browser'] == 'chrome':
        driver = Chrome()
    else:
        raise Exception(
            f'"{config["browser"]}" is not a supported browser'
        )

    driver.implicitly_wait(config['wait_time'])
    yield driver
    driver.quit()

def test_refactored_browser_search(browser):
    PHRASE = 'Pandaren'
    
    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    results_page = GoogleResultsPage(browser)
    assert results_page.result_div_count() > 0
    assert results_page.search_input_value() == PHRASE

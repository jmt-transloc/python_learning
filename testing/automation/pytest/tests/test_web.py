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

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The configuration file does not contain "browser"')
    elif config['browser'] not in ['chrome']:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else 10
#
# Create a browser fixture. Fixtures are called once per test function
# unless otherwise specified.
#
@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome()
    else:
        raise Exception(
            f'"{config["browser"]}" is not a supported browser'
        )

    driver.implicitly_wait(config_wait_time)
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

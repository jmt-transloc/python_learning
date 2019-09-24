# test_web
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

#
# Create a browser fixture. Fixtures are called once per test function
# unless otherwise specified.
#
@pytest.fixture
def browser():
    driver = Chrome() # establishes a driver instance of Chrome
    driver.implicitly_wait(10) # declare a wait of 10 for elements
    yield driver # returns a reference to the driver
    driver.quit() # quit out the driver once tests are complete

def test_basic_browser_search(browser):
    URL = 'https://www.google.com'
    PHRASE = 'Pandaren'
    
    browser.get(URL)
    
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(PHRASE + Keys.RETURN)
    
    result_divs = browser.find_elements_by_class_name('rc')
    assert len(result_divs) > 0

    search_field = browser.find_element_by_name('q')
    assert search_field.get_attribute('value') == PHRASE
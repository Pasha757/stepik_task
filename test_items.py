from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_is_button_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = WebDriverWait(browser, 15).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[type="submit"]')))
    assert len(button) > 0


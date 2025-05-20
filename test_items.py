from selenium.webdriver.common.by import By

def test_is_button_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, "button[value = 'Add to basket']")


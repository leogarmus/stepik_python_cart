from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    basket_button = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']/button")
    WebDriverWait(browser, 12).until(EC.visibility_of(basket_button))
    # login_link.click()
    assert basket_button.text == 'Añadir al carrito', "Should be Añadir al carrito"

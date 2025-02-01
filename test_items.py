import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_exist_button_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    basket_button = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']/button")
    WebDriverWait(browser, 12).until(EC.visibility_of(basket_button))
    
    # time.sleep(30) // Для проверки условия 2. Запустите тест с параметром --language=fr и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".
    assert basket_button.text == 'Añadir al carrito', "Should be Añadir al carrito"


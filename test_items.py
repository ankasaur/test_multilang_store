from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_is_present(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket'), "Add to basket button is not found"
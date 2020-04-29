from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    INNER_CONTENT = (By.CSS_SELECTOR, "#content_inner")
    CONTENT = (By.CSS_SELECTOR, "#basket_formset")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TOTAL_BASKET = (By.CSS_SELECTOR, '.alert-info p strong')
    ITEM_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_ITEM_IN_BASKET = (By.CSS_SELECTOR, ".alert:first-child .alertinner strong")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main h1 ")

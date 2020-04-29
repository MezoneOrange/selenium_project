from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty_text(self):
        message = self.browser.find_element(*BasketPageLocators.INNER_CONTENT).text
        text = message.split('.')[0].strip()
        assert text == "Your basket is empty", f"{text} not equal 'Your basket is empty'"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT), \
            "Success message is presented, but should not be"

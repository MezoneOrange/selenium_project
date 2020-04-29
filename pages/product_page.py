from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def item_should_be_into_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM).text.lower()
        item_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_BASKET).text.lower()
        assert item_name == item_name_in_basket, "item name '{}' != item in basket '{}'".format(item_name,
                                                                                                item_name_in_basket)

    def basket_value_and_item_value_should_be_same(self):
        item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST).text
        basket_cost = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET).text
        assert item_cost == basket_cost, "item cost {} != basket cost {}".format(item_cost, basket_cost)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_BASKET), \
            "Success message is presented, but should not be"

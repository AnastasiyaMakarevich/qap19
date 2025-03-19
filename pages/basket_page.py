import time
import allure
from pages.base_page import BasePage
from locators.basket_locators import BasketPageLocators


class BasketPage(BasePage, BasketPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open basket page')
    def open_basket(self):
        time.sleep(2)
        self.click(self.BUTTON_BASKET)

    @allure.step('Assert that basket is empty')
    def assert_that_basket_is_empty(self):
        self.assertions.assert_that_text_is_the_same(self.BASKET_IS_EMPTY, 'Корзина пуста')

    @allure.step('Assert that basket is not empty')
    def assert_that_basket_is_not_empty(self):
        self.assertions.assert_that_element_doesnt_exist(self.BASKET_IS_EMPTY)

    @allure.step('Click make order')
    def click_make_order(self):
        time.sleep(2)
        self.click(self.BUTTON_MAKE_ORDER)

    @allure.step('Assert that make order is working')
    def assert_that_make_order_is_working(self):
        self.assertions.assert_that_text_is_the_same(self.MAKE_ORDER_FIELD, 'Оформление заказа')

    @allure.step('Set promocode')
    def set_promocode(self, promocode):
        self.fill(self.PROMO_CODE, promocode)

    @allure.step('Click use promocode')
    def click_use_promocode(self):
        time.sleep(1)
        self.click(self.BUTTON_USE_PROMO_CODE)

    @allure.step('Assert that promocode is incorrect')
    def assert_that_promocode_is_incorrect(self):
        self.assertions.assert_that_element_is_visible(self.PROMO_CODE_IS_INVALID)

    @allure.step('Return product text by index')
    def get_product_text_by_index(self, i):
        return self.get_element_by_index(self.PRODUCT_TEXT, i).text

    @allure.step('Delete from basket by index')
    def delete_from_basket_by_index(self, i):
        time.sleep(1)
        self.get_element_by_index(self.BUTTON_DELETE_PRODUCT, i).click()
        self.click(self.BUTTON_CONFIRM_DELETE_PRODUCT)

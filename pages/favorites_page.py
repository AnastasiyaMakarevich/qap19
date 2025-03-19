import time
import allure
from pages.base_page import BasePage
from locators.favorites_locators import FavoritesPageLocators
from selenium.common.exceptions import NoSuchElementException


class FavoritesPage(BasePage, FavoritesPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open favorites page')
    def open_favorites(self):
        time.sleep(1)
        self.click(self.BUTTON_FAVORITES)

    @allure.step('Return text from favorites by index')
    def get_text_from_favorites_by_index(self, i):
        return self.get_element_by_index(self.FAVORITES_PRODUCTS_TEXT, i).text

    @allure.step('Delete from favorites by index')
    def delete_from_favorites_by_index(self, i):
        self.get_element_by_index(self.BUTTON_DELETE_FROM_FAVORITES, i).click()

    @allure.step('Assert that favorites is empty')
    def assert_that_favorites_is_empty(self):
        assert self.is_element_visible(
            self.NO_FAVORITES_MESSAGE), "Сообщение о пустых избранных товарах не отображается"

    @allure.step('Assert that favorites is not empty')
    def assert_that_favorites_is_not_empty(self):
        assert self.is_element_visible(self.FAVORITES_HEADER), "Заголовок 'Избранные товары' не отображается"

    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()  # Проверяем, видим ли элемент
        except NoSuchElementException:
            return False

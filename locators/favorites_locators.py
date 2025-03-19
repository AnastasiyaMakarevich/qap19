from selenium.webdriver.common.by import By


class FavoritesPageLocators:
    BUTTON_FAVORITES = (By.XPATH, '//a[@href="/aside/"][1]')
    FAVORITES_PRODUCTS_TEXT = (By.CSS_SELECTOR, '[class="CardInfo_info__zKUou Favorite_info__M_w9F"]')
    BUTTON_DELETE_FROM_FAVORITES = [By.CSS_SELECTOR, '[class="LinkButton-module__wrapper LinkButton-module__body '
                                                     'LinkButton-module__regular LinkButton-module__pink"]']

    NO_FAVORITES_MESSAGE = (By.CSS_SELECTOR, '[class="FavoritesScreen_content__MMSka"]')
    FAVORITES_HEADER = (By.CSS_SELECTOR, '[class="FavoritesScreen_title__TY942 Title-module__title Title-module__h1"]')

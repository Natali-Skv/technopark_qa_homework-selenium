from selenium.webdriver.common.by import By


class BasePageLocators:
    CART_BUTTON = (By.ID, "shoppingCartButton")
    CART = (By.CLASS_NAME, "shopping-cart")
    GUAVA_RESTAURANT_IMG = (By.XPATH, '//img[@class="rest-icon__rest_img" and @alt="Guava"]')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "dish-icon__button-add-to-order")
    ORDER_BUTTON = (By.ID, "orderButton")
    PAY_BUTTON = (By.ID, "buttonPay")
    LOGO_BUTTON = (By.XPATH, '//a[@class="main-button__controller" and text() = "obringTo"]')
    ORDER_HISTORY_HEADER = (By.XPATH, '//h1[@class="form-title__title-name" and text() = "Мои заказы"]')
    PROMOCODE_IMG = (By.CLASS_NAME, "promo-code-block__promo-code-icon")
    DETAILS_BUTTON = (By.CLASS_NAME, "buttonOpenClose")
    ORDER_DETAILS = (By.CLASS_NAME, "order__main-content")
    SEND_REVIEW_BUTTON = (By.XPATH, '//*[@id="commentButton"]/button')
    SEND_REVIEWS_HEADER = (By.XPATH, '//h1[@class="simple-title" and contains(text(),"Оставить отзыв о")]')


class HeaderLocators(BasePageLocators):
    LOGIN_MODAL = (By.ID, "modal")
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    GUAVA_RESTAURANT_IMG = (By.XPATH, '//img[@class="rest-icon__rest_img" and @alt="Guava"]')
    PROFILE_MENU = (By.CLASS_NAME, "profile-preview__menu")
    ADDRESS_INPUT = (By.ID, "suggestsSearch")
    SUGGESTS = (By.CLASS_NAME, "suggest-form__suggest-row")
    LAST_SUGGEST = (By.XPATH, '//div[@class="suggest-form__suggest-row"][last()]')
    LOGO_BUTTON = (By.XPATH, '//a[@class="main-button__controller" and text() = "obringTo"]')
    LOGIN_BUTTON = (By.XPATH, '//nav[@data-section="login"]')
    SEARCH_BUTTON = (By.ID, "searchButton")
    SEARCH_CLOSE_BUTTON = (By.ID, "closeSearchImg")
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_AREA = (By.ID, "searchActivatedAria")
    CART_BUTTON = (By.ID, "shoppingCartButton")
    CART = (By.CLASS_NAME, "shopping-cart")
    RESTAURANTS_HEADER = (By.XPATH, '//a[@class="links-block__main-link" and text() = "Рестораны"]')


class MainPageLocators(BasePageLocators):
    MENU_HEADER = (By.XPATH, '//h1[@class="simple-title"]')
    PROMOCODE_IMG = (By.CLASS_NAME, "promo-code-block__promo-code-icon")
    PROMOCODE_UI_NOTIFICATION = (By.XPATH, '//div[@class="notification__message" and text() = "Промокод успешно применен"]')
    SUSHI_CATEGORY_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and @data-title = "Суши"]')
    SUSHI_CATEGORY_SELECTED_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and contains(@class, "category_selected") and @data-title = "Суши"]')
    PIZZA_CATEGORY_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and @data-title = "Пицца"]')
    PIZZA_CATEGORY_SELECTED_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and contains(@class, "category_selected") and @data-title = "Пицца"]')


class LoginLocators(BasePageLocators):
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    LOGIN_MODAL = (By.ID, "modal")
    PHONE_INPUT = (By.XPATH, '//div[@id="loginPhone"]//input[@class="input-block__input"]')
    EMPTY_PHONE_ERROR = (By.XPATH, '//div[@id="loginPhone"]//div[@class="input-block__input-underline error" and text() = "Заполните это поле"]')
    PHONE_LENGTH_ERROR = (By.XPATH, '//div[@id="loginPhone"]//div[@class="input-block__input-underline error" and text() = "Формат телефона: +7(988)888-88-88"]')
    NOT_REGISTERED_PHONE_ERROR = (By.XPATH, '//div[@id="loginPhone"]//div[@class="input-block__input-underline error" and text() = "Номер не зарегистрирован"]')
    LOGIN_BUTTON = (By.ID, "loginButton")
    REGISTER_BUTTON = (By.ID, "registerButton")
    CODE_INPUT = (By.XPATH, '//div[@id="confirmCode"]//input[@class="input-block__input"]')
    CONFIRM_CODE_BUTTON = (By.ID, "confirmCodeButton")
    CONFIRM_CODE_HEADER = (By.XPATH, '//h2[@class="preview__title" and text()="Подтвердите телефон"]')
    CLOSE_BUTTON = (By.ID, "closeImg")
    RETRY_BUTTON = (By.ID, "sendCodeButton")
    RETRY_SUCCESS = (By.XPATH, '//div[@class="notification__message" and text() = "Ожидайте звонок"]')
    INVALID_CODE_ERROR = (By.XPATH, '//div[@id="confirm-code-form"]//div[@class="input-block__input-underline error" and text() = "Неверный код подтверждения"]')
    CLOSE_BUTTON = (By.ID, "closeImg")


class RestaurantMenuLocators(BasePageLocators):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "dish-icon__button-add-to-order")
    CART = (By.CLASS_NAME, "shopping-cart")
    ALL_RESTAURANTS_BUTTON = (By.CLASS_NAME, "back-button")
    RESTAURANTS_LIST = (By.CLASS_NAME, "restaurants-form")


class CartLocators(BasePageLocators):
    ADD_TO_CART_BUTTON = [
        (By.XPATH, "(//button[contains(@class,'dish-icon__button-add-to-order')])[1]"),
        (By.XPATH, "(//button[contains(@class,'dish-icon__button-add-to-order')])[2]"),
    ]
    CART = (By.CLASS_NAME, "shopping-cart")
    DECREMENT_DISH_COUNT = [
        (By.XPATH, "(//img[@class='decrementDishCount'])[1]"),
        (By.XPATH, "(//img[@class='decrementDishCount'])[2]"),
    ]
    INCREMENT_DISH_COUNT = [
        (By.XPATH, "(//img[contains(@class,'incrementDishCount')])[1]"),
        (By.XPATH, "(//img[contains(@class,'incrementDishCount')])[2]"),
    ]
    COUNT_OF_DISH_IN_CART = [
        (By.XPATH, "(//div[contains(@class,'point-info__count-current-point')])[1]"),
        (By.XPATH, "(//div[contains(@class,'point-info__count-current-point')])[2]"),
    ]
    DISH_IN_CART = [
        (By.XPATH, '(//section[contains(@class,"shopping-cart__order-point")])[1]'),
        (By.XPATH, '(//section[contains(@class,"shopping-cart__order-point")])[2]'),
    ]
    ORDER_BUTTON = (By.ID, "orderButton")
    PRICE_OF_DISH_IN_CART = [
        (By.XPATH, "(//div[contains(@class,'dish-info__price-bold')])[1]"),
        (By.XPATH, "(//div[contains(@class,'dish-info__price-bold')])[2]"),
    ]
    PRICE_OF_DISH_IN_MENU = [
        (By.XPATH, "(//div[@class='dish-icon__price-bar']/div[contains(text(),'₽')])[1]"),
        (By.XPATH, "(//div[@class='dish-icon__price-bar']/div[contains(text(),'₽')])[2]"),
    ]


class RecommendationsLocators(BasePageLocators):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "dish-icon__button-add-to-order")
    RECOMMENDATIONS = (By.CLASS_NAME, "shopping-cart__recommendations")
    ADD_RECOMMENDATIONS = (By.CLASS_NAME, "recommendation__button-add-to-order")
    RECOMMENDATION_DISH_IN_CART = (By.XPATH, '//*[@id="modal"]/div/div[2]/section[2]')


class PromoCodesLocators(BasePageLocators):
    PROMO_CODE = (By.CLASS_NAME, "promo-code-block__promo-code-icon")
    PROMO_CODE_RESET = (By.CLASS_NAME, "shopping-cart__preview-rest")


class ReviewsLocators(BasePageLocators):
    REVIEW_INFO_BLOCK = (By.CLASS_NAME, "comments-block__value")
    SEND_REVIEW_BUTTON = (By.CLASS_NAME, "review-button")
    REVIEWS_HEADER = (By.XPATH, '//h1[@class="simple-title" and contains(text(),"Отзывы о")]')
    REVIEWS = (By.CLASS_NAME, "comment")
    REVIEW_TEXTAREA = (By.ID, "comment")
    REVIEW_STARS_BUTTONS = [
        (By.XPATH, '//img[contains(@class,"star") and @data-count="1"]'),
        (By.XPATH, '//img[contains(@class,"star") and @data-count="2"]'),
        (By.XPATH, '//img[contains(@class,"star") and @data-count="3"]'),
        (By.XPATH, '//img[contains(@class,"star") and @data-count="4"]'),
        (By.XPATH, '//img[contains(@class,"star") and @data-count="5"]'),
    ]
    SEND_REVIEW_CONTENT_BUTTON = (By.ID, "createComment")
    REVIEW_TEXT = (By.CLASS_NAME, "comment__text")
    REVIEW_STARS = (By.CLASS_NAME, "comment__stars")


class RegisterLocators(BasePageLocators):
    PHONE_INPUT = (By.XPATH, '//div[@id="register-form"]//div[@id="registerPhone"]//input[@class="input-block__input"]')
    NAME_INPUT = (By.XPATH, '//div[@id="register-form"]//div[@id="registerName"]//input[@class="input-block__input"]')
    EMAIL_INPUT = (By.XPATH, '//div[@id="register-form"]//div[@id="registerEmail"]//input[@class="input-block__input"]')
    EMPTY_PHONE_ERROR = (By.XPATH, '//div[@id="register-form"]//div[@id="registerPhone"]//div[@class="input-block__input-underline error" and text() = "Заполните это поле"]')
    EMPTY_NAME_ERROR = (By.XPATH, '//div[@id="register-form"]//div[@id="registerName"]//div[@class="input-block__input-underline error" and text() = "Заполните это поле"]')
    EMPTY_EMAIL_ERROR = (By.XPATH, '//div[@id="register-form"]//div[@id="registerEmail"]//div[@class="input-block__input-underline error" and text() = "Заполните это поле"]')
    PHONE_LENGTH_ERROR = (By.XPATH, '//div[@id="register-form"]//div[@id="registerPhone"]//div[@class="input-block__input-underline error" and text() = "Формат телефона: +7(988)888-88-88"]')
    INVALID_EMAIL_ERROR = (By.XPATH, '//div[@id="register-form"]//div[@id="registerEmail"]//div[@class="input-block__input-underline error" and text() = "Формат email: fobrinto@gmail.com"]')
    REGISTERED_PHONE_ERROR = (By.XPATH, '//div[@class="notification__message" and text() = "Пользователь с таким номером уже зарегистрирован"]')
    REGISTER_BUTTON = (By.ID, "register-button")
    LOGIN_BUTTON = (By.XPATH, '//div[@id="register-form"]//button[@class="simple-button" and @data-section="login"]')
    CLOSE_BUTTON = (By.ID, "closeImg")
    CONFIRM_CODE_HEADER = (By.XPATH, '//h2[@class="preview__title" and text()="Подтвердите телефон"]')


class ProfileLocators(BasePageLocators):
    AVATAR_INPUT = (By.ID, "avatarUpload")
    AVATAR_BUTTON = (By.ID, "changeAvatarButton")
    NAME_INPUT = (By.XPATH, '//form[@id="person-info-form"]//div[@id="profileName"]//input[@class="input-block__input"]')
    EMAIL_INPUT = (By.XPATH, '//form[@id="person-info-form"]//div[@id="profileEmail"]//input[@class="input-block__input"]')
    SAVE_BUTTON = (By.ID, "personInfoSaveButton")
    EMPTY_NAME_ERROR = (By.XPATH, '//form[@id="person-info-form"]//div[@id="profileName"]//div[@class="input-block__input-underline error" and text() = "Заполните это поле"]')
    EMPTY_EMAIL_ERROR = (By.XPATH, '//form[@id="person-info-form"]//div[@id="profileEmail"]//div[@class="input-block__input-underline error" and text() = "Заполните это поле"]')
    SAVE_SUCCESS = (By.XPATH, '//div[@class="notification__message" and text() = "Изменения успешно сохранены"]')
    ORDER_HISTORY_BUTTON = (By.XPATH, '//form[@id="person-info-form"]//div[@data-section="orderHistory"]')
    BACK_BUTTON = (By.XPATH, '//form[@id="person-info-form"]/a/img')


class LogoutLocators(BasePageLocators):
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    LOGOUT_BUTTON = (By.XPATH, '//section[@id="modal"]//div[@class="profile-menu__point logoutButton"]')


class OrderingLocators(BasePageLocators):
    BACK_BUTTON = (By.XPATH, '//header[@id="header"]//a/img')
    PAY_BUTTON = (By.ID, "buttonPay")
    SAVE_SUCCESS = (By.XPATH, '//div[@class="notification__message" and text() = "Заказ успешно создан"]')


class OrderHistoryLocators(BasePageLocators):
    DETAILS_BUTTON = (By.CLASS_NAME, "buttonOpenClose")
    ORDER_DETAILS = (By.CLASS_NAME, "order__main-content")
    GO_TO_ALL_RESTAURANTS = (By.CLASS_NAME, "back-button__img")
    RESTAURANTS_HEADER = (By.XPATH, '//a[@class="links-block__main-link" and text() = "Рестораны"]')


class SearchPageLocators(BasePageLocators):
    SEARCH_BUTTON = (By.ID, "searchButton")
    SEARCH_CLOSE_BUTTON = (By.ID, "closeSearchImg")
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_AREA = (By.ID, "searchActivatedAria")
    RESTAURANT_CART = (By.CLASS_NAME, "restaurants-form__rest_icon")
    RESTAURANT_CART_NAME = (By.CLASS_NAME, "rest-icon__rest-name")
    NOTHING_FOUND_MESSAGE = (By.XPATH, '//div[@class="restaurants-form__empty-rest-list" and contains(text()," ничего не найдено. Попробуйте ввести другой ресторан или категорию")]')
    TOO_LONG_UI_NOTIFICATION = (By.XPATH, '//div[@class="notification__message" and text() = "Извините, но название ресторана не может превышать 100 символов."]')
    UI_NOTIFICATION = (By.XPATH, '//div[@class="notification__message"]')


class SuggestPageLocators(BasePageLocators):
    ADDRESS_INPUT = (By.ID, "suggestsSearch")
    SUGGESTS = (By.CLASS_NAME, "suggest-form__suggest-row")
    LAST_SUGGEST = (By.XPATH, '//div[@class="suggest-form__suggest-row"][last()]')

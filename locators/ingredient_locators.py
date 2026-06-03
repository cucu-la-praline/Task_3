from selenium.webdriver.common.by import By


class IngredientLocators:
    INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "(//button[contains(@class, 'Modal_modal__close')])[1]")
    OPEN_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")


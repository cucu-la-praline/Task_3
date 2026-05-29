from selenium.webdriver.common.by import By


class IngredientLocators:
    # Общий локатор для ингредиентов
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")

    def get_ingredient_by_name(self, name):
        return (By.XPATH, f"//a[contains(@class, 'BurgerIngredient_ingredient')]//p[text()='{name}']/..")

    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal_close')]")

    def get_ingredient_counter(self, name):
        return (By.XPATH,
                f"//a[contains(@class, 'BurgerIngredient_ingredient')]//p[text()='{name}']/../..//p[contains(@class, 'counter')]")

    CONSTRUCTOR_INGREDIENT = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_ingredient')]")
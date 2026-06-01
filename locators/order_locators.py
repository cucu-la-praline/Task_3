from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2")
    YOUR_HAS_BEEN_PREPARED = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    COMPL_IN_ALL_TIME = (By.XPATH,  "//p[text()='Выполнено за все время:']/parent::div/p[contains(@class, 'OrderFeed')]")
    COMPL_TODAY = (By.XPATH, "//p[text()='Выполнено за все время:']/parent::div/p[contains(@class, 'OrderFeed')]")
    IN_WORK = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]")

    @staticmethod
    def order_item(index):
        return By.XPATH, f"(//ul[contains(@class, 'OrderFeed_list')]/li/a)[{index}]"

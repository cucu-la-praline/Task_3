from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FEED_LIST = (By.XPATH, "//div[contains(@class, 'OrderFeed_list')]")
    ORDER_IN_FEED = (By.XPATH, "//div[contains(@class, 'OrderFeed_list')]//div[contains(@class, 'OrderFeed_item')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    COMPLETED_COUNTER = (By.XPATH, "//div[contains(@class, 'OrderFeed_completed')]//p[@class='OrderFeed_number']")
    TODAY_COMPLETED_COUNTER = (By.XPATH, "//div[contains(@class, 'OrderFeed_completed')]//p[@class='OrderFeed_number'][2]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2")
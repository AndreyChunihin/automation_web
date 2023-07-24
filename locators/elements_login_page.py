from selenium.webdriver.common.by import By

class StartPage:
    LOGIN = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')



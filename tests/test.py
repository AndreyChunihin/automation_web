from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver

# Find and interact with First Name field
def test_first_name():
    first_name_locator = 'input[name="firstName"]'
first_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, first_name_locator)))
first_name_input.clear()
first_name_input.send_keys('Andrey')

# Find and interact with Middle Name field
middle_name_locator = 'input[name="middleName"]'
middle_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, middle_name_locator)))
middle_name_input.clear()
middle_name_input.send_keys('Qa')

# Find and interact with Last Name field
last_name_locator = 'input[name="lastName"]'
last_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, last_name_locator)))
last_name_input.clear()
last_name_input.send_keys('QA')

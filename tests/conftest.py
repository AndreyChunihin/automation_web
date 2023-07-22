import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    # Create Chrome WebDriver instance
    driver_options = Options()
    #driver_options.add_argument('--incognito')  # Add any other options you need
    chrome_driver_version = "114.0.5735.90"  # Замените это на нужную версию
    driver = webdriver.Chrome(ChromeDriverManager(version=chrome_driver_version).install(), options=driver_options)
    driver.set_window_size(1280, 800)

    driver_options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 "
                                "Firefox/84.0")

    yield driver

    # Quit the WebDriver after the test
    driver.quit()

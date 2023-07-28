import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginAction



@pytest.fixture()
def driver():
    # Create Chrome WebDriver instance
    driver_options = Options()
    # driver_options.add_argument('--incognito')  # Add any other options you need
    chrome_driver_version = "114.0.5735.90"
    driver = webdriver.Chrome(ChromeDriverManager(version=chrome_driver_version).install(), options=driver_options)
    driver.set_window_size(1280, 800)

    driver_options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 "
                                "Firefox/84.0")

    yield driver

    # Quit the WebDriver after the test
    driver.quit()


@pytest.fixture
def login_and_open_dashboard(driver):
    login = LoginAction(driver, 'https://opensource-demo.orangehrmlive.com/')
    login.open()
    login.fill_fields_login()
    dashboard_page = DashboardPage(driver,
                                   'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    dashboard_page.open()
    return dashboard_page

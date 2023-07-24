import time


def test_example(driver):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    driver.get(url)
    time.sleep(4)

import time
import inspect

from selenium.webdriver.common.by import By
from classes.Webdriver import Webdriver
from tools import log

logger = log.setup(__name__)


def main():
    logger.debug(inspect.stack()[0][3])

    driver_ = Webdriver()
    driver = driver_.get_driver()

    driver.get("https://www.whatsmyip.org/")
    time.sleep(3)
    print(driver.page_source)


main()

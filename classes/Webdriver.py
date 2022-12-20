from classes.DriverOptions import DriverOptions
from selenium import webdriver


class Webdriver(DriverOptions):
    def __init__(self):
        DriverOptions.__init__(self)

    def get_driver(self):
        driver = webdriver.Chrome(
            executable_path=self.path, options=self.get_options())
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })
        return driver

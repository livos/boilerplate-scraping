from classes.Settings import Settings
from classes.UserAgentsGenerator import UserAgentsGenerator
from classes.Proxy import Proxy
from selenium.webdriver.chrome.options import Options


class DriverOptions(Settings, Proxy, UserAgentsGenerator):

    def __init__(self):
        Settings.__init__(self)
        Proxy.__init__(self)
        UserAgentsGenerator.__init__(self)

    def get_options(self):

        self.options = Options()

        # self.options.add_argument('--headless')

        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")

        if self.use_proxy:
            self.options.add_argument('--proxy-server=%s' % self.get_proxy())

        if self.use_user_agent:
            self.options.add_argument('user-agent=%s' % self.get_user_agent)

        return self.options

import os


class Settings(object):
    def __init__(self, use_proxy=False, use_user_agent=False, path=os.path.join(os.getcwd(), '..drivers\chromedriver.exe')):
        self.use_proxy = use_proxy
        self.use_user_agent = use_user_agent
        self.path = path

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def switch_to_next_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
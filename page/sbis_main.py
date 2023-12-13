from page.base_page import BasePage
from selenium.webdriver.common.by import By


class SbisMainPage(BasePage):
    def go_to_contacts_page(self):
        contacts_link = self.browser.find_element(By.CSS_SELECTOR, "#wasaby-content > div > div > div.sbis_ru-Region.bodyContent__zIndex-context > div.sbis_ru-content > div.sbisru-Header-sticky.sbisru-Header--font.sbisru-Header__scheme--default > div.sbisru-Header > div.sbisru-Header__container.sbis_ru-container > ul > li.sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm > a")
        contacts_link.click()


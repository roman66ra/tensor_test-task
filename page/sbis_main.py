from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisMainPage(BasePage):
    def go_to_contacts_page(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                  "#wasaby-content > div > div > div.sbis_ru-Region.bodyContent__zIndex-context > div.sbis_ru-content > div.sbisru-Header-sticky.sbisru-Header--font.sbisru-Header__scheme--default > div.sbisru-Header > div.sbisru-Header__container.sbis_ru-container > ul > li.sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm > a")))
        contacts_link = self.browser.find_element(By.CSS_SELECTOR,
                                                  "#wasaby-content > div > div > div.sbis_ru-Region.bodyContent__zIndex-context > div.sbis_ru-content > div.sbisru-Header-sticky.sbisru-Header--font.sbisru-Header__scheme--default > div.sbisru-Header > div.sbisru-Header__container.sbis_ru-container > ul > li.sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm > a")
        contacts_link.click()

    def go_to_download_page(self):
        download_link = self.browser.find_element(By.CSS_SELECTOR,
                                                  "#container > div.sbisru-Footer.sbisru-Header__scheme--default > div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(10) > ul > li:nth-child(6) > a")
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", download_link)
        download_link.click()

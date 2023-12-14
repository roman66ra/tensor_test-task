from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisContactsPage(BasePage):
    def go_to_tensor_page(self):
        tensor_link = self.browser.find_element(By.CSS_SELECTOR,
                                                "#contacts_clients div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 img")
        tensor_link.click()

    def check_region(self):
        region = self.browser.find_element(By.CSS_SELECTOR,
                                           "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span")
        assert region.text == "Республика Башкортостан"

    def check_partners(self):
        self.browser.find_element(By.CSS_SELECTOR, "div.sbisru-Contacts-List__col")

    def check_change_region(self):
        region = self.browser.find_element(By.CSS_SELECTOR,
                                           "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span")
        first_region = region.text
        region.click()

        self.browser.find_element(By.CSS_SELECTOR,
                                  "#popup > div.controls-Popup.ws-float-area-show-complete.controls_themes__wrapper.controls-Scroll_webkitOverflowScrollingTouch.controls-Popup__lastItem.undefined.controls-Popup_shown > div > div > div > div > div.sbis_ru-Region-Panel > div > ul > li:nth-child(43) > span").click()

        WebDriverWait(self.browser, 50).until(EC.title_contains("Камчатский край"))
        WebDriverWait(self.browser, 50).until(EC.url_changes("41-kamchatskij-kraj"))

        region = self.browser.find_element(By.CSS_SELECTOR,
                                           "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span")

        current_url = self.browser.current_url

        assert "https://sbis.ru/contacts/41-kamchatskij-kraj" in current_url
        assert region != first_region
        assert region.text == "Камчатский край"

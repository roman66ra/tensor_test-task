import time
import os
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisDownload(BasePage):
    def download_sbis_plugin(self):
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body.sbis-ru-CookieAgreement-visible')))
        self.browser.find_element(By.CSS_SELECTOR, 'div[data-id="plugin"]').click()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a")))

        text_windows = self.browser.find_element(By.CSS_SELECTOR,
                                                 'div[data-name="items[1].content"] div[data-component= "SBIS3.CONTROLS/Tab/Button"] span:nth-child(1)')
        windows_checked = self.browser.find_element(By.CSS_SELECTOR,
                                                    'div[data-name="items[1].content"] div[data-component= "SBIS3.CONTROLS/Tab/Button"]:nth-child(1)')
        assert text_windows.text == "Windows" and "controls-Checked__checked" in windows_checked.get_attribute('class')

        link_for_download = self.browser.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a")
        link_for_download.click()

    def waiting_and_check_download_file(self):
        while True:
            try:
                open('sbisplugin-setup-web.exe')
                break
            except:
                time.sleep(.1)

        path = os.getcwd()
        file_size = os.path.getsize(path + '/sbisplugin-setup-web.exe')

        assert file_size == 7362168

    def delete_file(self):
        file = os.getcwd() + '/sbisplugin-setup-web.exe'
        os.remove(file)

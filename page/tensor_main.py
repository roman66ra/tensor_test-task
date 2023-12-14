from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TensorMainPage(BasePage):
    def should_be_block_strength_is_in_people(self):
        self.browser.find_element(By.CSS_SELECTOR,
                                  '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div')

    def go_to_tensor_about_link(self):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")))
        about_link = self.browser.find_element(By.CSS_SELECTOR,
                                               "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(about_link))
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", about_link)
        about_link.click()

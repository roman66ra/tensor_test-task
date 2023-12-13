from page.base_page import BasePage
from selenium.webdriver.common.by import By


class TensorAboutPage(BasePage):
    def check_elements_size(self):
        elements = self.browser.find_elements(By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")
        elements_size = []
        len_elements = len(elements)

        for i in range(len_elements):
            elements_size.append(elements[i].size)

        counter = 0

        for i in range(len_elements):
            if elements_size[i] == {'height': 309, 'width': 435}:
                counter +=1

        assert counter == len(elements_size)






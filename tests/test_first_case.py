from page.sbis_main import SbisMainPage
from page.sbis_contacts import SbisContactsPage
from page.tensor_main import TensorMainPage
from page.tensor_about import TensorAboutPage


def test_first_case(browser):
    url_sbis = "https://sbis.ru/"
    url_sbis_contacts = "https://sbis.ru/contacts"
    url_tensor = "https://tensor.ru/"
    url_tensor_about = "https://tensor.ru/about"

    page_sbis = SbisMainPage(browser, url_sbis)
    page_sbis_contacts = SbisContactsPage(browser, url_sbis_contacts)
    page_tensor = TensorMainPage(browser, url_tensor)
    page_tensor_about = TensorAboutPage(browser, url_tensor_about)

    page_sbis.open()
    page_sbis.go_to_contacts_page()
    page_sbis_contacts.go_to_tensor_page()

    browser.switch_to.window(browser.window_handles[1])

    page_tensor.should_be_block_strength_is_in_people()
    page_tensor.go_to_tensor_about_link()

    page_tensor_about.check_elements_size()

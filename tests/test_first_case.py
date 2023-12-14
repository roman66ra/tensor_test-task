from page.sbis_main import SbisMainPage
from page.sbis_contacts import SbisContactsPage
from page.tensor_main import TensorMainPage
from page.tensor_about import TensorAboutPage
from constants import URL_SBIS, URL_SBIS_CONTACTS, URL_TENSOR, URL_TENSOR_ABOUT


def test_first_case(browser):
    page_sbis = SbisMainPage(browser, URL_SBIS)
    page_sbis_contacts = SbisContactsPage(browser, URL_SBIS_CONTACTS)
    page_tensor = TensorMainPage(browser, URL_TENSOR)
    page_tensor_about = TensorAboutPage(browser, URL_TENSOR_ABOUT)

    page_sbis.open()
    page_sbis.go_to_contacts_page()
    page_sbis_contacts.go_to_tensor_page()

    page_sbis_contacts.switch_to_next_window()

    page_tensor.should_be_block_strength_is_in_people()
    page_tensor.go_to_tensor_about_link()

    page_tensor_about.check_elements_size()

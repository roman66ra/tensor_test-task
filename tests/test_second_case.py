from page.sbis_contacts import SbisContactsPage
from constants import URL_SBIS_CONTACTS


def test_second_case(browser):
    page_sbis_contacts = SbisContactsPage(browser, URL_SBIS_CONTACTS)

    page_sbis_contacts.open()
    page_sbis_contacts.check_region()
    page_sbis_contacts.check_partners()
    page_sbis_contacts.check_change_region()

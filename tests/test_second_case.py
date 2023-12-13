from page.sbis_contacts import SbisContactsPage


def test_second_case(browser):
    url_sbis_contacts = "https://sbis.ru/contacts"

    page_sbis_contacts = SbisContactsPage(browser, url_sbis_contacts)

    page_sbis_contacts.open()
    page_sbis_contacts.check_region()
    page_sbis_contacts.check_partners()
    page_sbis_contacts.check_change_region()

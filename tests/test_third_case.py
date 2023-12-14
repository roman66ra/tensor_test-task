from page.sbis_main import SbisMainPage
from page.sbis_download import SbisDownload


def test_third_case(browser):
    url_sbis = "https://sbis.ru/"
    url_sbis_download = "https://sbis.ru/download"

    page_sbis = SbisMainPage(browser, url_sbis)
    page_sbis_download = SbisDownload(browser, url_sbis_download)

    page_sbis.open()
    page_sbis.go_to_download_page()
    page_sbis_download.download_sbis_plugin()
    page_sbis_download.waiting_and_check_download_file()
    page_sbis_download.delete_file()

from page.sbis_main import SbisMainPage
from page.sbis_download import SbisDownload
from constants import URL_SBIS, URL_SBIS_DOWNLOAD


def test_third_case(browser):
    page_sbis = SbisMainPage(browser, URL_SBIS)
    page_sbis_download = SbisDownload(browser, URL_SBIS_DOWNLOAD)

    page_sbis.open()
    page_sbis.go_to_download_page()
    page_sbis_download.download_sbis_plugin()
    page_sbis_download.waiting_and_check_download_file()
    page_sbis_download.delete_file()

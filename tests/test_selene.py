from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

OWN_URL = "https://github.com/"
URL_NAME = "IrinaVorontsova/qa_guru_4_9"
ISSUE = "#13"


def test_github():
    browser.open(OWN_URL)

    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(URL_NAME)
    browser.element(".header-search-input").submit()

    browser.element(by.link_text(URL_NAME)).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text(ISSUE)).should(be.visible)

    browser.quit()

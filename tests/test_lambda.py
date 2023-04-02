import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


OWN_URL = "https://github.com/"
URL_NAME = "IrinaVorontsova/qa_guru_4_9"
ISSUE = "#13"

def test_github():
    with allure.step(f"Open own page {OWN_URL}"):
        browser.open(OWN_URL)

    with allure.step(f"Search repo {URL_NAME}"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys(URL_NAME)
        browser.element(".header-search-input").submit()

    with allure.step(f"Move to repo {URL_NAME}"):
        browser.element(by.link_text(URL_NAME)).click()

    with allure.step("Move to issues panel"):
        browser.element("#issues-tab").click()

    with allure.step(f"Check the issue number {ISSUE}"):
        browser.element(by.partial_text(ISSUE)).should(be.visible)

    with allure.step("Close browser"):
        browser.quit()

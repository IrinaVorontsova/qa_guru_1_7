import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

OWN_URL = "https://github.com/"
URL_NAME = "IrinaVorontsova/qa_guru_4_9"
ISSUE = "#13"

def test_decorator():
    open_own_page(OWN_URL)
    search_pero(URL_NAME)
    move_to_repo(URL_NAME)
    move_to_issues()
    check_issue_for_number(ISSUE)
    close_browser()

@allure.step("Open own page {page}")
def open_own_page(page):
    browser.open(page)


@allure.step("Search repo {repo}")
def search_pero(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()

@allure.step("Move to repo {repo}")
def move_to_repo(repo):
    browser.element(by.link_text(repo)).click()

@allure.step("Move to issues panel")
def move_to_issues():
    browser.element("#issues-tab").click()

@allure.step("Check the issue number {issue}")
def check_issue_for_number(issue):
    browser.element(by.partial_text(issue)).should(be.visible)

@allure.step("Close browser")
def close_browser():
    browser.quit()

from selene import have, be
from selene.support.shared import browser
from allure import step as title

from mobile_tests_lesson_13.model import app


def test_move_between_screens():
    app.given_opened()

    with title('Search for content'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('selene')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))

    with title('Open an article'):
        browser.element('«Ancient Greek goddess of the Moon»').tap()
        browser.element('#view_page_header_image').should(be.visible)

    with title('Open language screen'):
        browser.element('#page_language').tap()
        browser.element('«Other languages»').should(be.visible)

    with title('Search language'):
        browser.element('#menu_search_language').tap()
        browser.element('#search_src_text').type('russian')

    with title('Tap on language'):
        browser.element('#localized_language_name').tap()
        browser.element('#view_page_header_image').should(be.visible)

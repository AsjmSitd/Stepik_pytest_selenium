import time

link = r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(5)
    element = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(element) == 1, f'The button "{element}" is not present or selector is not valid, length is: {len(element)}'




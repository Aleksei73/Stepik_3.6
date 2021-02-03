import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    x = 0
    try:
        browser.find_element_by_css_selector('button[class*="btn-add-to-basket"]')
        x = 1
    except Exception:
        pass
    finally:
        assert x == 1, 'Элемент не найден'

'''
Такой вариант использовался для того чтобы выводилась ошибка описанная в assert, был вариант
assert browser.find_element_by_css_selector('button[class*="btn-add-to-basket"]'), "Элемент не найден"
Но тогда будет выходить ошибка самого селениума, а не описанная в assert
'''

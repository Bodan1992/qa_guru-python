# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def function_name(func):
    print('Имя функции:','', func.__name__ )
    if func.__code__.co_varnames:
        print('Аргументы функции:',)
    else:
        print('Нет аргументов')
    for arg in func.__code__.co_varnames:
        print(' ' + arg)



def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def support():
    return None

functions_all = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page,support)
for i in functions_all:
    function_name(i)
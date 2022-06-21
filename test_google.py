
# пример из лекции
# import pytest
#
# @pytest.fixture()                                      # decorator(декоратор)
# def before_each(request):
#     print("Called before each test " + request.node.name)               # request.node.name-проверка правда ли запускается фикстура перед каждым тестом
#
# @pytest.fixture(scope='session',autouse=True)                                      # decorator(декоратор)/ scope='session-вызывается для каждой сессии
# def init_browser(request):                                                         #autouse=True-не явная инициализация(запуск в каждом тесте)
#     print("Called before all tests " + request.node.name)
#
# @pytest.fixture()
# def message():
#     return "This is message"
#

# @pytest.fixture()
# def client():
#     print(123)
#     yield                                           #запуск
#     print("А теперь удаляем клиента")
#
#
# def test_first(before_each):
#     assert 1 == 1
#
# def test_second(before_each):
#     assert 1 == 2, "Единица не должна быть равна двойке!"
#
#
# def test_message(message,firefox):
#     print(message)
#     assert "message" in message
#
# def test_client(client):
#     assert client == 123



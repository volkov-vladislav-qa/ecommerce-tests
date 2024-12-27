import pytest

@pytest.fixture()
def set_up():
    print("\nЗапуск теста")    #перед тестом

    yield    #сам тест

    print("\nТест завершен!")    #после теста
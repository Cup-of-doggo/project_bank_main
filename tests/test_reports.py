from src.reports import log


@log()
def hello_world():
    """функция для теста"""
    print("Hello, world!")


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, world!\nhello_world все ок \nРезультат: None\n'

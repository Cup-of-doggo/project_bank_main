from freezegun import freeze_time

from src.utils import greetings


@freeze_time('2025.01.01')
def test_greetings():
    greetings()
    assert "Доброй ночи"
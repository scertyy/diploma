from os import getenv


def _l(env_key):
    """ Загрузить переменную или выкинуть ошибку"""
    env_value = getenv(env_key)
    if env_value is None:
        raise AssertionError(f'Не было передано значение {env_key} в переменные окружения.')
    return env_value

from typing import Callable


def create_handlers(callback: Callable[[int], any]) -> list:
    return [lambda: callback(step) for step in range(5)]


def execute_handlers(handlers: list):
    for handler in handlers:
        handler()

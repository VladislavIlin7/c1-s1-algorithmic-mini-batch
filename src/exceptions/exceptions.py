class ApplicationError(Exception):
    """Базовая ошибка"""
    def __init__(self, error: str):
        super().__init__(f"{error}")

class StackIsEmptyError(ApplicationError):
    def __init__(self):
        super().__init__("Стэк пуст")

class CmpAndKeyTogetherError(ApplicationError):
    def __init__(self):
        super().__init__("Нельзя одновременно передавать key и cmp")
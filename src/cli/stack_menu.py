from src.exceptions.exceptions import StackIsEmptyException
from src.structures.stack import Stack


def stack_menu() -> None:
    """
    Подменю для работы со стеком
    """

    stack = Stack()

    print("\nСоздан новый пустой стек")

    while True:
        print("\n=== Меню стека ===")
        print("Команды:")
        print("  push X   - положить число X в стек")
        print("  pop      - снять верхний элемент")
        print("  peek     - посмотреть верхний элемент")
        print("  min      - показать минимум в стеке")
        print("  len      - показать размер стека")
        print("  empty    - проверить пуст ли стек")
        print("  back     - вернуться в главное меню")

        cmd = input("> ").strip().split()

        if not cmd:
            continue

        action = cmd[0]

        if action == "back":
            break

        if action == "push":
            if len(cmd) != 2:
                print("Использование: push 10")
                continue
            try:
                x = int(cmd[1])
            except ValueError:
                print("Нужно целое число")
                continue
            stack.push(x)
            print(f"Добавлено {x} в стек")

        elif action == "pop":
            try:
                value = stack.pop()
                print(f"Снят элемент: {value}")
            except StackIsEmptyException as e:
                print(f"Ошибка: {e}")

        elif action == "peek":
            try:
                value = stack.peek()
                print(f"Верхний элемент: {value}")
            except StackIsEmptyException as e:
                print(f"Ошибка: {e}")

        elif action == "min":
            try:
                value = stack.min()
                print(f"Минимум в стеке: {value}")
            except StackIsEmptyException as e:
                print(f"Ошибка: {e}")

        elif action == "len":
            print(f"Размер стека: {len(stack)}")

        elif action == "empty":
            print("Стек пуст" if stack.is_empty() else "В стеке есть элементы")

        else:
            print("Неизвестная команда")
__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    a = sum([i for i in arr if not i % 2])
    b = sum([i for i in arr if i % 2])
    try:
        res = a/b
    except ZeroDivisionError:
        return 0
    return res

print(even_odd([1, 2, 3, 4, 5]))

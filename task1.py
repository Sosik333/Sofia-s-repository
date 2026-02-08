# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Box:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param length: Длина коробки, см
        :param width: Ширина коробки, см
        :param height: Высота коробки, см

        Примеры:
        >>> box = Box(50, 30, 8)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина коробки должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина коробки должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина коробки должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина коробки должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота коробки должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота коробки должна быть положительным числом")
        self.height = height


    def is_box_square(self) -> bool:
        """
        Функция которая проверяет является ли коробка квадратной))

        :return: Является ли коробка квадратной

        Примеры:
        >>> box = Box(50, 50, 4)
        >>> box.is_box_square()
        """
        ...

    def volume_calculation(self) -> float:
        """
        Расчет объема коробки.

        :return: Объем заданной коробки

        Примеры:
        >>> box = Box(50, 30, 8)
        >>> box.volume_calculation()
        """
        ...

class Note:
    def __init__(self, color: str, sheets: float):
        """
        Создание и подготовка к работе объекта "Блокнот"

        :param color: Цвет
        :param sheets: Количество страниц

        Примеры:
        >>> note = Note("Blue", 48)  # инициализация экземпляра класса
        """
        if not isinstance(color, (str)):
            raise TypeError("Цвет должен быть типа str")
        self.color = color
        if not isinstance(sheets, (int, float)):
            raise TypeError("Количество страниц должно быть типа int или float")
        if sheets <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.sheets = sheets


    def is_enough(self, need_sheets: float) -> bool:
        """
        Функция которая проверяет хватит ли блокнота на семестр))

        :param need_sheets: Необходимое количество страниц для конспекта

        :return: Подойдет ли блокнот для конспекта

        Примеры:
        >>> note = Note("Red", 4)
        >>> note.is_enough(48)
        """
        if not isinstance(need_sheets, (int, float)):
            raise TypeError("Количество страниц должно быть типа int или float")
        if need_sheets < 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        ...

    def tear_pages(self, teared_pages) -> None:

        """
        Функция вырывания листов из блокнота.

        :param teared_pages: Объем извлекаемой жидкости
        :raise ValueError: Если количество вырываемых страниц превышает количество страниц в блокноте,
        то возвращается ошибка.

        Примеры:
        >>> note = Note("Green", 50)
        >>> note.tear_pages(2)
        """
        ...


class Salary:
    def __init__(self, volume: float):
        """
        Создание и подготовка к работе объекта "Зарплата"

        :param volume: Величина зарплаты, руб

        Примеры:
        >>> salary = Salary(180000)  # инициализация экземпляра класса
        """
        MROT = 16000

        if not isinstance(volume, (int, float)):
            raise TypeError("Величина зарплаты должна быть типа int или float")
        if volume <= MROT:
            raise ValueError("Зарплата ниже прожиточного минимума")
        self.volume = volume

    def is_enough_for_vacation(self, need_money: float) -> bool:
        """
        Функция которая проверяет хватит ли блокнота на семестр))

        :param need_money: Необходимое количество денег на отпуск

        :return: Получится ли накопить на отпуск за год

        Примеры:
        >>> salary = Salary(30000)
        >>> salary.is_enough_for_vacation(250000)
        """
        if not isinstance(need_money, (int, float)):
            raise TypeError("Цена отпуска должна быть типа int или float")
        if need_money < 0:
            raise ValueError("Цена отпуска должна быть положительным числом")
        ...

    def increase_salary(self, money) -> None:
        """
        Функция поднятия зарплаты.

        :param money: Надбавка к зарплате

        Примеры:
        >>> salary = Salary(50000)
        >>> salary.increase_salary(200000)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

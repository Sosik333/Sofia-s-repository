class Pen:
    """
    Базовый класс Ручка.

    Объединяет общие свойства и поведение для всех типов ручек.
    Атрибут _ink_level сделан защищенным, чтобы предотвратить прямое изменение
    уровня чернил, минуя логику их расходования.
    """

    def __init__(self, brand: str, color: str, ink_capacity: float) -> None:
        """
        Инициализируем базовую ручку.

        Аргументы:
            brand: Производитель ручки.
            color: Цвет чернил.
            ink_capacity: Вместимость чернил.
        """
        self.brand = brand
        self.color = color
        self._ink_level = ink_capacity

    def write(self, text: str):
        """
        Метод для письма: ручка пишет, если есть чернила.

        Аргументы:
            text: Текст, который нужно написать.

        Возвращает:
            Написанный текст или None, если писать невозможно.
        """
        if self._ink_level <= 0:
            print("Чернила закончились.")
            return None

        # Расход чернил
        self._ink_level -= len(text) * 0.1
        return f"Ручка {self.brand} пишет: {text}"

    def __str__(self) -> str:
        return f"Ручка бренда {self.brand}, цвет чернил: {self.color}"

    def __repr__(self) -> str:
        return (f"Pen(brand='{self.brand}', color='{self.color}', "
                f"ink_level={self._ink_level:.1f})")


class Ballpen(Pen):
    """
    Дочерний класс шариковой ручки.

    Добавляет новый атрибут tip_size - размер шарика.
    """

    def __init__(self, brand: str, color: str, ink_capacity: float, tip_size: float) -> None:
        """
        Аргументы:
            brand: Производитель ручки.
            color: Цвет чернил.
            ink_capacity: Вместимость чернил.
            tip_size: Размер шарика в миллиметрах.
        """
        super().__init__(brand, color, ink_capacity)
        self.tip_size = tip_size

    def write(self, text: str):
        """
        Перегружает метод родительского класса.

        Причина:
        Шариковые ручки пишут бледнее, когда пасты остается очень мало.
        """

        if self._ink_level <= 0:
            print("Паста закончилась.")
            return None

        # Учитываем особенности шариковой ручки: расход чернил меньше при малом остатке
        if self._ink_level < 2.0:
            consumption = len(text) * 0.05
            print("Чернил мало, ручка пишет бледнее.")
        else:
            consumption = len(text) * 0.1

        self._ink_level -= consumption
        return f"Шариковая ручка {self.brand} ({self.tip_size}мм) пишет: {text}"

    def __str__(self) -> str:
        return f"{super().__str__()}, тип: шариковая, {self.tip_size}мм"


class FountainPen(Pen):
    """
    Дочерний класс перьевой ручки.

    Добавляет атрибут nib_material - материал пера.
    """

    def __init__(self, brand: str, color: str, ink_capacity: float, nib_material: str) -> None:
        """
        Аргументы:
            brand: Производитель ручки.
            color: Цвет чернил.
            ink_capacity: Вместимость чернил.
            nib_material: Материал пера (например, "сталь").
        """
        super().__init__(brand, color, ink_capacity)
        self.nib_material = nib_material

    def write(self, text: str):
        """
        Перегружает метод родительского класса.

        Причина:
        Перьевые ручки расходуют больше чернил, но пишут равномерно, вне зависимости от
        остатка чернил.
        """
        if self._ink_level <= 0:
            print("Чернила закончились.")
            return None

        # Учитываем особенности перьевой ручки: больший расход чернил
        self._ink_level -= len(text) * 0.15
        return (f"Перьевая ручка {self.brand} (перо: {self.nib_material}) "
                f"пишет: {text}")

    def refill(self, ink_color: str) -> None:
        """
        Новый метод, специфичный для перьевых ручек - заправка чернилами.
        В нем изменяем защищенный атрибут _ink_level.

        Аргументы:
            ink_color: Цвет новых чернил.
        """
        self._ink_level = 100.0  # условно полная заправка
        self.color = ink_color
        print(f"Перьевая ручка заправлена чернилами цвета {ink_color}.")

    def __str__(self) -> str:
        return f"{super().__str__()}, тип: перьевая, перо: {self.nib_material}"


if __name__ == "__main__":
    # Пример с шариковой ручкой
    bp = Ballpen("Parker", "синий", 50.0, 0.7)
    print(bp.write("Hello, World!"))

    # Пример с перьевой ручкой
    fp = FountainPen("Montblanc", "черный", 30.0, "сталь")
    print(fp.write("Hello, World!"))
    fp.refill("красный")
    print(fp)


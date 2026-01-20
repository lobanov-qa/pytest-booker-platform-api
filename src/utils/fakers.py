from faker import Faker

from datetime import date, timedelta
from typing import Optional


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр Faker для генерации данных.
        """
        self.faker = faker

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)
    
    
    def booking_dates(
        self,
        checkin: Optional[date] = None,
        delta: int = 1,
        max_days_ahead: int = 90  # например, максимум 3 месяца вперёд
    ) -> dict:
        """
        Генерирует валидный словарь bookingdates с checkin и checkout.
        Обеспечивает, что checkout > checkin, и checkin не слишком далёкий.

        :param checkin: Дата заезда. Если None — берётся случайная дата в ближайшие max_days_ahead.
        :param delta: Разница между checkout и checkin в днях (минимум 1).
        :param max_days_ahead: Максимальное количество дней вперёд для checkin.
        :return: Словарь вида {"checkin": "2025-04-01", "checkout": "2025-04-02"}.
        """
        # Если checkin не передан — выбираем случайную дату в ближайшие max_days_ahead
        if checkin is None:
            random_offset = self.faker.random_int(min=1, max=max_days_ahead)
            checkin = date.today() + timedelta(days=random_offset)

        # Убедимся, что delta >= 1
        delta = max(delta, 1)
        checkout = checkin + timedelta(days=delta)

        return {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat()
        }


    def room_id(self) -> int:
        """
        Генерирует валидный roomid (целое число ≥1).

        :return: Случайный roomid.
        """
        return self.integer(1, 100)  

    def phone(self) -> str:
        """
        Генерирует валидный телефон (11–21 символ).
        Пример: +79123456789

        :return: Случайный номер телефона.
        """
        phone_number = self.faker.phone_number()
        while len(phone_number) < 11:
            phone_number = self.faker.phone_number()
        return phone_number[:21]

    def first_name(self, min_length: int = 3, max_length: int = 18) -> str:
        """
        Генерирует имя с учётом ограничений длины.

        :param min_length: Минимальная длина.
        :param max_length: Максимальная длина.
        :return: Имя в диапазоне длины.
        """
        name = self.faker.first_name()
        # Убедимся, что длина в пределах
        while len(name) < min_length or len(name) > max_length:
            name = self.faker.first_name()
        return name

    def last_name(self, min_length: int = 3, max_length = 30) -> str:
        """
        Генерирует фамилию с учётом ограничений длины.

        :param min_length: Минимальная длина.
        :param max_length: Максимальная длина.
        :return: Фамилия в диапазоне длины.
        """
        name = self.faker.last_name()
        while len(name) < min_length or len(name) > max_length:
            name = self.faker.last_name()
        return name

    def deposit_paid(self) -> bool:
        """
        Генерирует значение для depositpaid.

        :return: Случайное булево значение.
        """
        return self.faker.boolean()

    def email(self, domain: str | None = "example.com") -> str:
        """
        Переопределили с domain по умолчанию, чтобы избежать None.
        """
        return self.faker.email(domain=domain)

    def date_string(self, days_offset: int = 0) -> str:
        """Генерирует дату в формате YYYY-MM-DD."""
        target_date = date.today() + timedelta(days=days_offset)
        return target_date.isoformat()


# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())
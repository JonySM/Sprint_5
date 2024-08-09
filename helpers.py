import random


class Help:
    @staticmethod
    def generated_name():
        return f"Джони{random.randint(100, 999)}"
    @staticmethod
    def generated_email():
        return f"UserPrakticum{random.randint(100, 9999)}@yandex.ru"

    @staticmethod
    def generated_password():
        return f"UserPrakticum!*{random.randint(100, 9999)}"

    @staticmethod
    def generated_invalid_password():
        return f"U{random.randint(100, 999)}"











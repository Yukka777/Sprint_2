class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")


# Подкласс ExtendedCase
class ExtendedCase(Case):
    def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
        # вызываем конструктор суперкласса, чтобы задать базовые атрибуты
        super().__init__(test_case_id, name, step_description, expected_result)
        # добавляем новые атрибуты
        self.precondition = precondition
        self.environment = environment

    # переопределяем метод, чтобы дополнительно вывести новые атрибуты
    def print_test_case_info(self):
        # сначала вызываем метод суперкласса, чтобы вывести базовую информацию
        super().print_test_case_info()
        # выводим новые атрибуты
        print(f"\nПредусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")


# Создаём объект класса ExtendedCase с заданными параметрами
case = ExtendedCase('1',
                    'Наличие кнопки Принять',
                    '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ',
                    'Кнопка доступна',
                    'Открыть сервис',
                    'Яндекс Браузер')

# Вызываем метод для вывода информации
case.print_test_case_info()

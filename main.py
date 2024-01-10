import re

def validate_home_phone(phone_number):
    # Регулярний вираз для перевірки домашнього номера телефону (тільки цифри та довжина номера)
    pattern = r'^\d{10}$'

    # Перевірка відповідності регулярному виразу
    return bool(re.match(pattern, phone_number))

# Приклад використання:
phone_number1 = "0447305594"
phone_number2 = "332124"  # Невірна довжина

result1 = validate_home_phone(phone_number1)
result2 = validate_home_phone(phone_number2)

print(f"Результат для {phone_number1}: {result1}")  # Очікується True
print(f"Результат для {phone_number2}: {result2}")  # Очікується False

# Мобільний номер телефону
def validate_mobile_phone(phone_number):
    # Регулярний вираз для перевірки мобільного номера телефону (тільки цифри, можлива наявність плюса, довжина номера)
    pattern = r'^\+?\d{10,12}$'

    # Перевірка відповідності регулярному виразу
    return bool(re.match(pattern, phone_number))

# Приклад використання:
phone_number1 = "+380733507799"
phone_number2 = "0733507799"
phone_number3 = "+987654321"  # Невірна довжина

result1 = validate_mobile_phone(phone_number1)
result2 = validate_mobile_phone(phone_number2)
result3 = validate_mobile_phone(phone_number3)

print(f"Результат для {phone_number1}: {result1}")  # Очікується True
print(f"Результат для {phone_number2}: {result2}")  # Очікується True
print(f"Результат для {phone_number3}: {result3}")  # Очікується False

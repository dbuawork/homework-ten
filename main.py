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

# Email

def validate_email(email):
    # Регулярний вираз для перевірки електронної адреси
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]'

    # Перевірка відповідності регулярному виразу
    return bool(re.match(pattern, email))

# Приклад використання:
email1 = "user@example.com"
email2 = "invalid-email" # Невірний домен


result1 = validate_email(email1)
result2 = validate_email(email2)


print(f"Результат для {email1}: {result1}")  # Очікується True
print(f"Результат для {email2}: {result2}")  # Очікується False

# Пароль

def validate_password(password):
    # Регулярний вираз для перевірки пароля
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'

    # Перевірка відповідності регулярному виразу
    return bool(re.match(pattern, password))

# Приклад використання:
password1 = "StrongP@ssw0rd"
password2 = "weakpassword"
password3 = "NoDigitSymbol"

result1 = validate_password(password1)
result2 = validate_password(password2)
result3 = validate_password(password3)

print(f"Результат для {password1}: {result1}")  # Очікується True
print(f"Результат для {password2}: {result2}")  # Очікується False
print(f"Результат для {password3}: {result3}")  # Очікується Fals

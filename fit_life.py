# Проект FitLife - MVP версия 2.0

# 1. Сбор данных

# запрос имени
user_name = input("Добро пожаловать в FitLife! как вас зовут?\n")
# преобразование если пользователь ввел имя/фамилию не с заглавной
user_name = user_name.title()

# цикл для обработки ошибок, если ошибка, то возвращает к текущему запросу
while True:
    try:
        user_age = int(input("Введите ваш возраст: "))
        break
    except ValueError:
        print("Произошла ошибка! проверте ваш ввод!!")

while True:
    try:
        # запрос веса тип переменной - float
        user_weight = float(input("Введите ваш вес(в кг, отделите десятичную долю точкой!): "))
        break
    except ValueError:
        print("Произошла ошибка! проверте ваш ввод!!")

while True:
    try:
        # запрос роста тип переменной - float
        user_height = float(input("Введите ваш рост(в метрах, отделите десятичную долю точкой!): "))
        break
    except ValueError:
        print("Произошла ошибка! проверте ваш ввод!!")


# 2. используемые функции

def counting_bmi(user_weight, user_height):
    """Функция вычисления индекса массы тела (ИМТ)."""
    user_bmi = user_weight / (user_height ** 2)
    return round(user_bmi, 1)


def counting_water(user_weight):
    ml_water = 30
    ml_in_l = 1000
    """Функция вычисления нормы воды в литрах."""
    water_needed_ml = user_weight * ml_water
    return round(water_needed_ml / ml_in_l, 1)


# 3. вывод результатов

bmi_result = counting_bmi(user_weight, user_height)
water_result = counting_water(user_weight)

print(f'Привет, {user_name}!')
print(f'Вот ваш отчет: ')
print(f'Ваш возраст: {user_age}')
print(f'ИМТ(индекс массы тела): {bmi_result} кг/м2')
print(f'Ваша норма воды: {water_result} л')


print("Расчет окончен. Будьте здоровы!")

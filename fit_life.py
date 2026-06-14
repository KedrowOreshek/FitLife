# Проект FitLife - MVP версия 1.0


# 1. используемые функции

# функция вычисления ИМТ
def counting_bmi(user_weight, user_height):
    user_bmi = user_weight/(user_height ** 2)

    return round(user_bmi,1)

# функция вычисления нормы воды
def counting_water(user_weight):
    water_needed_ml = user_weight * 30

    return round(water_needed_ml / 1000, 1)

# 2. Сбор данных

# запрос имени
user_name = input("Добро пожаловать в FitLife! как вас зовут?\n")
user_name = user_name.title()   # преобразование если пользватель 
                                # ввел имя/фамилию не с заглавной 

# цикл для обработки ошибок, если ошибка, то возвращает к текущему запросу
while True:
    try:                                
        user_age = int(input("Введите ваш возраст: "))  # запрос возраста
        break
    except ValueError:
        print("Произошла ошибка! проверте ваш ввод!!")  # обработка ошибки 

while True:
    try:
        user_weight = float(input("Введите ваш вес(в кг): "))# запрос веса 
                                                             # тип переменной - float
        break
    except ValueError:
        print("Произошла ошибка! проверте ваш ввод!!")  # обработка ошибки 

while True:
    try:
        user_height = float(input("Введите ваш рост(в метрах): "))  # запрос роста 
                                                                # тип переменной - float
        break
    except ValueError:
        print("Произошла ошибка! проверте ваш ввод!!")  # обработка ошибки

# 3. вывод резултатов

print(
    f'Привет, {user_name}!\n'
    f'Вот ваш отчет: \n'
    f'Ваш возраст: {user_age}\n'
    f'ИМТ(индекс массы тела): {counting_bmi(user_weight, user_height)} кг/м²\n'
    f'Ваша норма воды: {counting_water(user_weight)} л'
)

print("Расчет окончен. Будьте здоровы!")
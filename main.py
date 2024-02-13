from math import pi
import random

x = int(input("Введите число x: "))
sum = 0
for i in range(1, x+1):
    sum += i
print(f"Сумма чисел от 1 до {x} равна", sum)

x = int(input("Введите число x: "))
sum = 0
for i in range(0, x+1):
    if i%2 != 0:
        sum += i
print(f"Сумма нечётных чисел от 0 до {x} равна", sum)

while True:
    x = (input("Введите слово (чтобы выйти из цикла, напишите Bye): "))
    if x == "Bye" or x == "bye":
        print("Эта часть программы окончена!")
        break

x = int(input("Введите номер месяца в году: "))
if x == 12 or x <= 2:
    print("Месяц с введённым вами номером относится к зимним.")
elif 3 <= x <= 5:
    print("Месяц с введённым вами номером относится к весенним.")
elif 6 <= x <= 8:
    print("Месяц с введённым вами номером относится к летним.")
elif 9 <= x <= 11:
    print("Месяц с введённым вами номером относится к осенним.")
else:
    print("Вы ввели несуществующий номер месяца.")

x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))
def less(x,y,z):
    sum = min(x,y,z)
    return sum

print(f"Наименьшее из введённых вами чисел — {less(x,y,z)}")

r = float(input("Введите радиус окружности: "))
def square_round(r):
    square_round = pi*r*r
    return square_round

print(f"Площадь круга с радиусом {r} равна {square_round(r)}")

list = ["Да", "Нет", "Не могу сейчас сказать"]
while True:
    x = input("Привет! Задай волнующий тебя вопрос, на которой можно ответить «Да» или «Нет»: ")
    if x != "Bye":
        print(random.choice(list))
    else:
        break























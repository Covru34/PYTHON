print("--- Завдяння 1 ---")

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінецб діапазону: "))

for number in range(start, end + 1):
    if number % 7 == 0:
        print("Числа які кратні 7: ", number)

print("--- Завдяння 2 ---")

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

myrange = range(start, end + 1) 

print("1) Усі числа діапазону:")
for i in range(start, end + 1):
    print(i, end=" ")
print()

print("2) Усі числа в спадному порядку:")
for i in range(end, start - 1, -1):
    print(i, end=" ")
print()

print("3) Чисоа які кратні 7: ")
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end="")

print("4) Кількість чисел кратних 5: ")
for i in range(start, end + 1):
    if i % 5 == 0:
        count += 1

print("4) Кількість чисел кратних 5: ", count)

print("--- Завдяння 3 ---")

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("--- Завдання 4 ---")

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
step = int(input("Введіть крок: "))

order = input("Введіть порядок (1 — прямий, 2 — зворотний): ")

if step <= 0:
    print("Крок повинен бути додатнім числом")
else:
    if order == "1":
        for i in range(start, end + 1, step):
            print(i)
    elif order == "2":
        for i in range(end, start - 1, -step):
            print(i)
    else:
        print("Неправильний вибір порядку")

print("--- Завдання 5 ---")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

# нормалізація діапазону
start = min(a, b)
end = max(a, b)

product = 1
found = False

for i in range(start, end + 1):
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        found = True

if found:
    print("Добуток чисел:", product)
else:
    print("Немає чисел, які діляться на 4, але не діляться на 6")

print("--- Завдання 5 ---")

A = int(input("Введіть число A: "))
N = int(input("Введіть степінь N: "))

result = 1

for _ in range(abs(N)):
    result *= A

if N < 0:
    result = 1 / result

print("Результат:", result)

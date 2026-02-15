# Завдання 1

numbers = list(map(int, input("Введіть список цілих чисел: ").split()))

for item in numbers:
    if(item % 2 == 0):
        print("Всі парні числа: ", item)

# Завдання 2

numbers = list(map(int, input("Введіть список цілих чисел: ").split()))

print("Максимальне число:", max(numbers))
print("Мінімальне число:", min(numbers))

# Завдання 3

numbers = [10, -9, 0, 5, -3]

min_positive = None
max_negative = None
positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
        if min_positive is None or num < min_positive:
            min_positive = num

    elif num < 0:
        negative_count += 1
        if max_negative is None or num > max_negative:
            max_negative = num

    else:
        zero_count += 1

print("Мінімальний додатній:", min_positive)
print("Максимальний від'ємний:", max_negative)
print("Кількість додатніх:", positive_count)
print("Кількість від'ємних:", negative_count)
print("Кількість нулів:", zero_count)

# Завдання 4

numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
a = int(input("Деяке число: "))

for num in numbers[:]:
    if num < a:
        numbers.remove(num)

print("Новий список:", numbers)
# Завадання 1
# Створив функцію def
# def count_greater_than_previous(list):
#     count = 0

#     for i in range(1, len(list)):
#         if list[i] > list[i-1]:
#             count += 1
#     return count

# # Викликав функцію def
# spisok = list(map(int, input("Введіть список цілих чисел: ").split()))

# result = count_greater_than_previous(spisok)
# print("Кількість елементів: ", result)

# # Завдання 2

# spisok = list(map(int, input("Введіть список цілих чисел: ").split()))

# print("Елементи які зустрічаються лише 1 раз: ")

# for i in spisok:
#     if spisok.count(i) == 1:
#         print(i, end=" ")

# # Завдання 3 

spisok = list(map(int, input("Введіть список цілих чисел: ").split()))

current = [spisok[0]]
longest = [spisok[0]]

for i in range(1, len(spisok)):
    if spisok[i] > spisok[i - 1]:
        current.append(spisok[i])
    else:
        current = [spisok[i]]

    if len(current) > len(longest):
        longest = current.copy()

print("Довжина:", len(longest))
print("Послідовність:", *longest)

# Завдання 4
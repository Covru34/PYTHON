print("Привіт, команда!")
# генерація послідовності чисел
items = range(5) # створили змінну items, яка зберігає послідовність
# items - зберігає числа віж 0 до 4
lengthItems = len(items) # lengthitems - зберігає довжину послідовності
# print("lenghtItems = ", lengthItems)
# цикл for для інтерації по послідовності
# Синтакси for:
#     блок коду для виконання
# цикл працює ітераціями - тобто тіло циклу (код у середину циклу)
# код, який працює у середині циклу буде мати відступ
for salo in items:  # перебираэмо елементи послідовності, що знаходяться в items
    print("item = ", salo) # Виводимо поточне значення змінної salo

print("Вкажіть діапазон чисел: ")
begin = int(input())
end = int(input())

print(f"begin = {begin}, end = {end}")

#генеруємо вказану послідовність чисел
myrange = range(begin, end) # створили послідовність чисел від begin до end
print("Ваша послідовність чисел: ")
for myitem in myrange: # цикл for перебирає послідовність myrange
    print(myitem, end="\t")

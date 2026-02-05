# Завданя 1

text = input("Введіть тест: ")

count = 0
for ch in text:
    if ch in ".!?":
        count +=1

print("Кількість речень:", count)

# Завдяння 2

text = input("Введи рядок: ")

clean = text.lower().replace(" ", "")
if clean == clean[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")

# Завдання 3

text = input("Введіть тест: ")
reserved = ["python", "if", "else", "for"]

words = text.split()
result = []

for  w in words:
    if w.lower() in reserved:
        result.append(w.upper())
    else:
        result.append(w)

print(" ".join(result))

# Завдання 4

text = input('Введіть текст: ')
a = input("Введіть преший символ: ")
b = input("Введіть другий символ: ")

start = text.find(a)
end = text.find(b, start + 1)

if start != -1 and end != -1:
    result = text[:start] + text[end+1:]
    print(result)
else:
    print("Символи не знайдені")
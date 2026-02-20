# Завдання 1

def writeInFiel():
    line1 = input("Надрукуйте перший рядок: ")
    line2 = input("Надрукуйте другий рядок: ")
    line3 = input("Надрукуйте третій рядок: ")

    fileWriter = open("data.txt", 'a', encoding="utf-8")

    fileWriter.write(f"{line1}\n")
    fileWriter.write(f"{line2}\n")
    fileWriter.write(f"{line3}\n")
    fileWriter.close()

writeInFiel()

# Завдання 2

# try:
#     with open("data.txt", "r", encoding="utf-8") as my:
#         lines = my.readlines() 

#         print("++Кожен другий рядок файлу data.txt++")

#         for i in range(1, len(lines), 2): 
#             print(lines[i].strip())

# except:
#     print("--Помилка роботи із файлом--")

# Завдання 3

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("filtered.txt", "w", encoding="utf-8") as new_file:
        for line in lines:
            if "Python" in line:
                new_file.write(line)

    print("Рядки з словом 'Python' записані у filtered.txt")

except FileNotFoundError:
    print("Файл data.txt не знайдено!")
except Exception as e:
    print("Сталася помилка:", e)

# Завдання 4

try:
    fielName = input("Введіть ім'я файлу: ")

    with open(fielName, "r", encoding="utf-8") as fiel:
        content = fiel.read()

    cleaned_content = "".join(char for char in content if not char.isdigit())

    with open("cleaned.txt", "w", encoding="utf-8") as new_file:
        new_file.write(cleaned_content)

    print("Готово")

except FileNotFoundError:
    print("Файл не знайдено")
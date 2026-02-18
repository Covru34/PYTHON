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

try:
    with open("data.txt", "r", encoding="utf-8") as my:
        lines = my.readlines() 

        print("++Кожен другий рядок файлу data.txt++")

        for i in range(1, len(lines), 2): 
            print(lines[i].strip())

except:
    print("--Помилка роботи із файлом--")
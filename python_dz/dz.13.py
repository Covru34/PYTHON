def personalityInfo():


    firstName = input("Введіть ваше ім'я: ")
    lastName = input("Введіть ваше призвіще: ")

    print(f"Ім'я:---{firstName}---")
    print(f"Призвіще:---{lastName}---")

def showNumbers(n):
    for i in range(n + 1):
        print(i, end=", " if i < n else "\n")

def min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    print("Мінімальне:", minimum)
    print("Максимальне:", maximum)
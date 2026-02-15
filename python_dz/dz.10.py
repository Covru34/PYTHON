# Просимо користувача ввести назву файлу
file_name = input("Введіть назву файлу: ")

try:
    # Відкриваємо файл у режимі читання
    with open(file_name, "r", encoding="utf-8") as file:
        # Читаємо вміст файлу
        content = file.read()
        # Виводимо вміст на екран
        print("\nВміст файлу:")
        print(content)
except FileNotFoundError:
    print("Файл не знайдено. Перевірте назву файлу.")
except Exception as e:
    print("Сталася помилка:", e)
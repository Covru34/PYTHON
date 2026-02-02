a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
choise = (input("Введіть дію яку потрібно виконати: додавання, віднімання, множення, ділення: "))

if choise == "додавання":
    c = a + b 
    print(f"{a} + {b} = {c}")
elif choise == "віднімання":
    c = a - b
    print(f"{a} - {b} = {c}")  
elif choise == "множення":
    c = a * b
    print(f"{a} * {b} = {c}")      
elif choise == "ділення":
    c = a / b
    print(f"{a} / {b} = {c}")    
else:
    print("Виберіть одну дію з наведених вище")
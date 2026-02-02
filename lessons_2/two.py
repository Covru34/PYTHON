text = "42\t42\t\t42"
print("text = ", text)

email = "mikola@gmail"
name = "Mykola"
string = f"name = {name}\temail = {email} " #перед рядком f означає що буде підстановка
print (string)

a = (input("Введіть а: "))
b = (input("Введіть b: "))
print(f"a = {a}\tb = {b}")

intA = float(a) # перетворили рядок до цілого числа intA
intB = float(b) 
c = intA + intB
print(f"a + b = {c}") #f буде підставляти змінну

c = intA - intB
print(f"a - b = {c}")
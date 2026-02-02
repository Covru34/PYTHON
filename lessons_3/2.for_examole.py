print("----Використання циклу for----")

ints = [23, 17, 5, 12] #Набір цілих чисел

for item in ints:
    print(f"item = {item}") #виводимо всі чмсла у односу рядку через табуляцію
print("Пошук парних чисел у послідовності")
for item in ints:
    if(item % 2 == 0):
        print(item, end = "\t")

# myint = 11
# if(myint % 2 == 0): 
#     print(f"{myint} - парне число")
# else:
#     print(f"{myint} - непарне число")
# Робимо функцію, яка буде реалізовувати калькулятор
def myCalc():
    a = input("Вкажіть значення a: ->_")
    b = input("Вкажіть значення b: ->_")
    intA = int(a)
    intB = int(b)
    print(f"{a}+{b}={intA+intB}") #f - форматований рядок у Python
    print(f"{a}-{b}={intA-intB}")
    print(f"{a}*{b}={intA*intB}")
    if intB!=0:
        print(f"{a}/{b}={intA/intB}")
    else:
        print("Маж спробу ділення 0")


# Робимо функцію, яка буде реалізовувати калькулятор
def myCalc():
    a = input("Вкажіть значення a: ->_")
    b = input("Вкажіть значення b: ->_")
    intA = int(a)
    intB = int(b)
    print(f"{a}+{b}={intA+intB}") #f - форматований рядок у Python
    print(f"{a}-{b}={intA-intB}")
    print(f"{a}*{b}={intA*intB}")
    # if intB!=0: 
    #     print(f"{a}/{b}={intA/intB}")
    # else:
    #     print("Має спробу діленняна 0")
    if intB==0: # == це порівнння
        print("Має спробу діленняна 0")
    else:
        print(f"{a}/{b}={intA/intB}")

#викли функції
myCalc()

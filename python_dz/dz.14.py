# Завдання 1

def print_quote():
    print('"Don\'t compare yourself with anyone in this world…')
    print('    if you do so, you are insulting yourself."')
    print('        Bill Gates')

print_quote()

# Завдання 2

def print_even(a, b):
    start = min(a, b)
    end = max(a, b)

    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

print_even(3, 12)

# Завдання 3

def draw_square(size, symbol, filled):
    for i in range(size):
        if filled:
            print(symbol * size)
        else:
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + " " * (size - 2) + symbol)

draw_square(5, "*", True)   # заповнений
draw_square(5, "*", False)  # порожній

# Завдання 4

def min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)

print(min_of_five(4, 7, 1, 9, 3))
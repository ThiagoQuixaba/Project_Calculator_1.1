#Limpar Terminal:
def Clean():
    from os import name
    from os import system
    sistema_operacional = name
    if sistema_operacional == 'posix':  # Para sistemas UNIX (Linux, macOS)
        system('clear')
    elif sistema_operacional == 'nt':  # Para Windows
        system('cls')

# Adição:
def Addition(num1, num2):
    try:
        return num1 + num2
    except:
        return '3RR0R 001!'

# Subtração:
def Subtraction(num1, num2):
    try:
        return num1 - num2
    except:
        return '3RR0R 002!'

# Multiplicação
def Multiplication(num1, num2):
    try:
        return num1 * num2
    except:
        return '3RR0R 003!'

# Divisão
def Division(dividend, divider):
    try:
        if divider != 0:
            return dividend / divider
        else:
            return 'Indeterminado'
    except:
        return '3RR0R 004!'

# Exponenciação:
def Exponentiation(base, exponent):
    try:
        return base ** exponent
    except:
        return '3RR0R 005!'
    
# Radiciação:
def Radiciation(rooting, index):
    try:
        if index >= 0:
            return (rooting ** (1 / index))
        elif index == 0:
            if rooting == 1:
                return "Ideterminado"
            else:
                return "3RR0R 006!"
        elif index < 0:
            return (1 / (rooting ** (1 / (index * -1))))
        else:
            return "3RR0R 007!"
    except:
        return "3RR0R 008!"

#logarithm:
def logarithm(logarithm, base):
    from math import log
    return log(logarithm, base)

#Fatorial:
def Factorial(num):
    try:
        if (isinstance(num, float) and num != int(num)) or num < 0:
            return "3RR0R 009!"
        elif num == 0:
            return 1
        else:
            num = int(num)
            result = 1
            for i in range(num, 0, -1):
                result *= i
            return result
    except:
        return "3RR0R 010!"
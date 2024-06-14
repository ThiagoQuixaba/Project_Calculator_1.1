import functions

def Menu1():
    while True:
        try:
            functions.Clean()
            print('---------------------------------------------------------------------------MENU--------------------------------------------------------------------------')
            value = int(input('Digite Um Numero: '))
            return value
        except:
            pass

def Menu2():
    while True:
        try:
            functions.Clean()
            print('---------------------------------------------------------------------------MENU--------------------------------------------------------------------------')
            print('| (+) -> Adição | (-) -> Subtração | (*) -> Multiplicação | (/) -> Divisão | (^) -> Potenciação | (r) -> Radiciação | (l) -> Logaritmo | (!) - Fatorial |')
            op = str(input('Digite Qual Operação Deseja Fazer: '))
            if op == '+' or op == '-' or op == '*' or op == '/' or op == '^' or op == 'r' or op == 'l' or op == '!':
                return op
            else:
                pass
        except:
            pass

def Menu3(num1, num2 = None, op = str):
    try:
        functions.Clean()
        print('---------------------------------------------------------------------------MENU--------------------------------------------------------------------------')
        match op:
            case '+':
                print(f'Sistema: {num1} + {num2} = {functions.Addition(num1, num2)}.')
            case '-':
                print(f'Sistema: {num1} - {num2} = {functions.Subtraction(num1, num2)}.')
            case '*':
                print(f'Sistema: {num1} * {num2} = {functions.Multiplication(num1, num2)}.')
            case '/':
                print(f'Sistema: {num1} / {num2} = {functions.Division(num1, num2)}.')
            case '^':
                print(f'Sistema: {num1} ^ {num2} = {functions.Exponentiation(num1, num2)}.')
            case 'r':
                print(f'Sistema: Raiz {num2}° de {num1} = {functions.Radiciation(num1, num2)}.')
            case 'l':
                print(f'Sistema: Log de {num1} na base {num2} = {functions.logarithm(num1, num2)}.')
            case '!':
                print(f'{num1}! = {functions.Factorial(num1)}.')
        input()
    except:
        pass

def Menu4():
    while True:
        try:
            functions.Clean()
            print('---------------------------------------------------------------------------MENU--------------------------------------------------------------------------')
            choice = str(input('Sistema: Deseja Continuar O Calculo? '))
            if choice.lower() == 's' or choice.lower() == 'sim' or choice.lower() == 'claro' or choice.lower() == 'blz' or choice.lower() == 'ok' or choice.lower() == 'y' or choice.lower() == 'yes' or choice.lower() == 'yeah':
                return True
            elif choice.lower() == 'n' or choice.lower() == 'não' or choice.lower() == 'nam' or choice.lower() == 'no' or choice.lower() == 'not':
                return False
            else:
                pass
        except:
            pass

def Menu5():
    while True:
        try:
            functions.Clean()
            print('---------------------------------------------------------------------------MENU--------------------------------------------------------------------------')
            choice = str(input('Sistema: Finalizar O Sistema? '))
            if choice.lower() == 's' or choice.lower() == 'sim' or choice.lower() == 'claro' or choice.lower() == 'blz' or choice.lower() == 'ok' or choice.lower() == 'y' or choice.lower() == 'yes' or choice.lower() == 'yeah':
                return True
            elif choice.lower() == 'n' or choice.lower() == 'não' or choice.lower() == 'nam' or choice.lower() == 'no' or choice.lower() == 'not':
                return False
            else:
                pass
        except:
            pass
import functions
import menus
values = [ '', '', '']
choices = ['', '']

while True:
    values[1] = menus.Menu1()
    while True:
        values[0] = menus.Menu2()
        match values[0]:
            case '+':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
            case '-':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
            case '*':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
            case '/':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
                if functions.Division(values[1], values[2]) == 'Indeterminado':
                    break
            case '^':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
            case 'r':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
                if functions.Radiciation(values[1], values[2]) == 'Indeterminado':
                    break
            case 'l':
                values[2] = menus.Menu1()
                menus.Menu3(values[1], values[2], values[0])
            case '!':
                menus.Menu3(values[1], values[2], values[0])

        choices[1] = menus.Menu4()
        if choices[1] == False:
            break
        else:
            match values[0]:
                case '+':
                    values[1] = functions.Addition(values[1], values[2])
                case '-':
                    values[1] = functions.Subtraction(values[1], values[2])
                case '*':
                    values[1] = functions.Multiplication(values[1], values[2])
                case '/':
                    values[1] = functions.Division(values[1], values[2])
                case '^':
                    values[1] = functions.Exponentiation(values[1], values[2])
                case 'r':
                    values[1] = functions.Radiciation(values[1], values[2])
                case 'l':
                    values[1] = functions.logarithm(values[1], values[2])
                case '!':
                    values[1] = functions.Factorial(values[1])
            pass

    choices[0] = menus.Menu5()
    if choices[0] == True:
        print('\nFinalizando Sistema...\nSistema Finalizado.')
        break
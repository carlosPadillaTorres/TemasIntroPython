import os

def run():
    op=0
    while op <5: 
        if op ==1:
            suma()
        if op==2:
            resta()
        if op ==3:
            multiplicacion()
        if op==4:
            division()
        else:
            l=input('Presione enter para continuar')
            os.system('cls')
            print('1. Suma')
            print('2. Resta')
            print('3. Multiplicación')
            print('4. División')
            print('5. Salir')
            op = int(input('Eliga una opción (númerica del menú): '))

    


def suma():
    #os.system('cls')
    print('Calculadora para sumar')
    num1 = int(input('Dame el primer número please: '))
    num2 = int(input('Dame el segundo número bro: '))
    res=num1+num2
    print(f'El resultado de la suma es: {res}')

def resta():
    #os.system('cls')
    print('Calculadora para restar')
    num1 = int(input('Dame el primer número please: '))
    num2 = int(input('Dame el segundo número bro: '))
    res=num1-num2
    print(f'El resultado de la resta es: {res}')


def multiplicacion():
    #os.system('cls')
    print('Calculadora para multiplicar')
    num1 = int(input('Dame el primer número please: '))
    num2 = int(input('Dame el segundo número bro: '))
    res=(num1)*(num2)
    print(f'El resultado de la multiplicación es: {res}')

def division():
    #os.system('cls')
    print('Calculadora para dividir')
    num1 = int(input('Dame el primer número please: '))
    num2 = int(input('Dame el segundo número bro: '))
    res=num1/num2
    print(f'El resultado de la división es: {res}')


if __name__ =="__main__":
    run()

''' if op ==1:
        suma()
    if op==2:
        resta()
    if op ==3:
        multiplicacion()
    if op==4:
        division()
    if op==5:
        print('Saliendo...')
    else:
        run()
'''
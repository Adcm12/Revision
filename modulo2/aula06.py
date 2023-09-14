from aula04 import soma, sustracao, multiplicacao, division

def menu():
    
    var = 1

    while var !=0:

        print('Digite cual operacion matematica deseja fazer')

        cond = int(input('1) Soma >> 2) Sustracao >> 3) Multiplicacion >> 4) Division >> 5)Sair >> '))

        match (cond):

            case 1:
                n1 = int(input('Digite su primer numero: '))
                n2 = int(input('Digite su segundo numero: '))
                print(soma(n1, n2))

                
            case 2:
                n1 = int(input('Digite su primer numero: '))
                n2 = int(input('Digite su segundo numero: '))
                print(sustracao(n1, n2))

            case 3:
                n1 = int(input('Digite su primer numero: '))
                n2 = int(input('Digite su segundo numero: '))
                print(multiplicacao(n1, n2))

            case 4:
                n1 = float(input('Digite su primer numero: '))
                n2 = float(input('Digite su segundo numero: '))
                print(division(n1, n2))

            case 5:
                var = 0

menu()


from time import sleep

inicio = int(input('Digite inicio '))
final = int(input('Digite o fin '))
passo = int(input('Digite o paso '))

for cronometro in range(inicio, final, -passo):
    sleep(1)
    print (cronometro)

cond = "sim"

while cond.lower() == 'sim':

    var = input('Digite su nombre para testar >> ')
    print(f'O nome digitado pelo usuario foi {var}')

    cond = input('Voce deseja continuar? \nsim \nnao \n >> ')

print('Voce saiu')
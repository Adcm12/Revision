from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica

menu = '\nDeseja cadastrar uma pessoa : \n1) Fisica \n2) Juridica \n3) Sair \n>>> '

while True:

    rodar = int(input(menu))

    match rodar:

        case 1:

            pf = PessoaFisica(
                input ('\nDigite o nome titular: '),
                input ('Digite o CPF do tituar: '),
                float(input ('Digite o saldo inicial: '))
            )
            print(pf)

            var = input('\nDeseja cadastrar o segundo titular: \nsim \nnao\n>> ')

            if var == 'sim':
                pf.segundo_titular = input ('\nDigite o segundo titular >>> ')
                print('\n', pf)
        case 2:

            pj = PessoaJuridica(
                input ('\nDigite o nome titular: '),
                input ('Digite o CPNJ da empresa: '),
                float(input ('Digite o saldo inicial: '))
            )
            print(pj)

            var = input('\nDeseja cadastrar o segundo titular: \nsim \nnao\n>> ')

            if var == 'sim':
                pj.segundo_titular = input ('\nDigite o segundo titular >>> ')
                print('\n', pj)
        case 3:
            break
from controller import create, read, update, search, delete

def menu():
    
    cond ='sim'
    while cond == 'sim':
        var = int(input('\n1) Criar \n2) Listar \n3) Pesquisar \n4) Alterar \n5) Deletar \n>> '))
        match(var):
            case 1:
                pessoa = {}
                pessoa["Nome"] = input("Digite seu nome: ").capitalize()
                pessoa["CPF"] = input("Digite seu cpf: ").capitalize()
                pessoa["Idade"] = input("Digite seu idade: ").capitalize()
                pessoa["Telefone"] = input("Digite seu telefone: ").capitalize()
                create(pessoa)

            case 2:
                read()
            
            case 3:
                search(input ('Digite o nome do cliente >> ').capitalize())

            case 4:
                update(input ('Digite o nome do cliente >> ').capitalize())

            case 5:
                delete(input ('Digite o nome do cliente >> ').capitalize())

        cond = input('\nDeseja continuar\n Sim \n Nao \n>> ').lower()
        
menu()


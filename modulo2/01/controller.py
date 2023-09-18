def create(a):

    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{a}\n')

def read():

    nomes = []

    with open('pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name= name.strip()
            nomes.append(name)

    
    return nomes

def buscar_nome(nome):
    
    nome_encontrado = []

    with open('pessoas.txt', 'r') as arquivo:
            
            for i in arquivo:

                i= i.strip()

                if (i == nome):
                        
                    nome_encontrado.append(i)

    if nome_encontrado:
        print(f'O nome esta na lista')
    
    else:
        print('Nome no esta na lista')
                      
                 
                



    





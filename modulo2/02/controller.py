import json
def create(cliente):
    with open("clientes.txt", "a") as arquivo:
        json.dump(cliente, arquivo)
        arquivo.write(f"\n")

def read():
    nomes = []
    with open('clientes.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip() #metodo
            nomes.append(name)

    for items in nomes:
        print(items)

def search(nome):

    with open('clientes.txt', 'r') as archivo:
        
        lineas = archivo.readlines()

        diccionario_encontrado = None

        for linea in lineas:
            
            diccionario = json.loads(linea)

            if "Nome" in diccionario and diccionario["Nome"] == nome:
                diccionario_encontrado = diccionario
                break  
        
        if diccionario_encontrado:

            print("Diccionario encontrado:")
            for clave, valor in diccionario_encontrado.items():
                print(f"\n{clave}: {valor}")
        else:
            print(f"No se encontró el nombre '{nome}' en el archivo.")


def update(cliente):
    flag = False

    with open('clientes.txt', 'r') as arquivo:
        lines = arquivo.readlines()

    with open('clientes.txt', 'w') as arquivo:
        for line in lines:
            if cliente in line:
                pessoa = {}
                pessoa["Nome"] = input("Digite seu novo nome: ").capitalize()
                pessoa["CPF"] = input("Digite seu novo cpf: ").capitalize()
                pessoa["Idade"] = input("Digite seu nova idade: ").capitalize()
                pessoa["Telefone"] = input("Digite seu novo telefone: ").capitalize()
                json.dump(pessoa, arquivo)
                arquivo.write(f"\n")
                flag = True
            else:
                arquivo.write(line)
    if flag:
        print('Seu arquivo foi alterado com sucesso!')

    else:
        print('Cliente nao encontrado!')

def delete(cliente):
    flag = False

    with open('clientes.txt', 'r') as arquivo:
        lines = arquivo.readlines()

    with open('clientes.txt', 'w') as arquivo:

        for line in lines:
            if cliente not in line:
                arquivo.write(line)
            else:
                flag = True  # Cliente encontrado e excluído


    if flag:
        print('Seu arquivo foi alterado com sucesso!')

    else:
        print('Cliente nao encontrado!')




# def search(c):
#     index = 0
#     flag = 0
#     arquivo = open('clientes.txt', 'r')
#     for line in arquivo:
#         index += 1
#         if c == eval(line)['Nome']:
#             print(line)
#             flag = 1

#         else:
#             flag == 0
#             print('Cliente não encontrado!')
from time import sleep

situacion = ' reprovado'

while situacion == " reprovado":

    nome = input('Digite su nome: ')
    sobrenome = input('Digite su sobrenome: ')
    idade = input('Digite su idade: ')

    lista_notas = []

    for lista in range(0, 4):
        nota = float(input('Digite su a nota: '))
        lista_notas.append(nota)
    media = sum(lista_notas) / len(lista_notas)

    if media < 7:

        situacion = 'reprovado'
        print(f'Infelizmente el alumno fue {situacion} con a media de {media}')

    if media >=7:
        situacion = 'aprovado'
        for c in  range(10):
            print('*')
            sleep(0.5)

        print(f'Parabens o aluno foi {situacion} con a media de {media}')

    dicionario = {

        "Nome":nome,
        "Sobrenome":sobrenome,
        "Idade":idade,
        "Nota":lista_notas,
        "Media":media,
        "Situacion":situacion
    }

    menu = input('Deseja ver lops dados do aluno? \nSim \nNao \n>> ')

    if menu.lower() == 'sim':

        print(f'''
        {dicionario["Nome"]}
        {dicionario["Sobrenome"]}
        {dicionario["Idade"]}
        {dicionario["Nota"]}
        {dicionario["Media"]}
        {dicionario["Situacion"]}
''')
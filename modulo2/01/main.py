from controller import create, read, buscar_nome

a = input('Digite su nome >> ')

create(a)

print(read())

a

buscar_nome(input('Digite o nome que vai procurar >> ').capitalize())


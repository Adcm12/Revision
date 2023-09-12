nome = input('Digite su nome >>')
idade = int(input('Digite su idade >>'))

nota1 = float(input('Digite su nota >>'))
nota2 = float(input('Digite su nota >>'))

media = (nota1 + nota2) / 2

alumno = {

    "Nome" : nome,
    "Idade" : idade,
    "Nota 1" : nota1,
    "Nota 2" : nota2,
    "Media" : media,

}

print(f"O nome do alumno e {alumno['Nome']} e sua media e {alumno['Media']}")
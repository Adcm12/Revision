# if e else ela utiliza de operadores racionales para exibir o ejecutar el codigo 
# Switch Case definida qque entra en una estructura de caso

# for e uma estructura de repeticion que cmposta por indice
# while ele uma estructura de repeticion que e baseada en operadores relaciones


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

cond = int(input(''' 
    Digite una opcion
    1) Nome
    2) Idade
    3) Nota 1
    4) Nota 2
    5) Media
    >>>>> 
                 '''))

if cond == 1:
    print("El nombre del alumno es",alumno["Nombre"])
    
elif cond == 2:
    print ("La edad de ",alumno['Nome'],"es:",alumno['Idade'])
elif cond ==3:
    print ('Su primera nota fue:',alumno ['Nota 1'] )
elif cond == 4:
    print ('Su segunda nota fue',alumno ["Nota 2"] )
elif cond == 5:
    print ('Su media fue ',alumno ["Media"], ' ')
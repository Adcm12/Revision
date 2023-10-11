class Tarea:

    def __init__(self, nombre, descripcion, fecha_ini, fecha_fin):

        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        lista_tareas = []

    def crear_tarea(self):

        tareas = [self.nombre, self.descripcion, self.fecha_ini, self.fecha_fin]
        Tarea.lista_tareas.append(tareas)
        print('Tarea creada con exito!!!')


    def listar_tareas():

        for i in Tarea.lista_tareas:
            print('\n', i)


tarea1 = Tarea('Prueba1', 'Dasssss', '05/05/05', '06/06/06')
tarea2 = Tarea('Prueba2', 'Desssss', '05/05/05', '06/06/06')
tarea3 = Tarea('Prueba3', 'Disssss', '05/05/05', '06/06/06')


tarea = tarea1.crear_tarea()
tarea = tarea2.crear_tarea()
tarea = tarea3.crear_tarea()

Tarea.listar_tareas()

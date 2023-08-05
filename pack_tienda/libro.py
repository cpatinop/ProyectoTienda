libros = []

class Libro:
    def __init__(self, nombre=" ", hojas=0, stock=0):
        self.nombre = nombre
        self.hojas = hojas
        self.stock = stock
        
    def Agregar_Libro(self, nombre, hojas, stock):
        self.nombre = nombre
        self.duracion = hojas
        self.stock = stock
        libros.append({"Libro": nombre,
                        "Hojas": hojas,
                        "stock": stock})
        
    def Listar_Libros(self):
        return libros

#l = Libro()
#l.Agregar_Libro("Los hermanos Grin", 210,23 )
#l.Agregar_Libro("Memorias", 510,18 )
#print (l.Listar_Libros())
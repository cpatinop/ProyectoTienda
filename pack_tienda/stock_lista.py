#from libro import Libro
#from pelicula import Pelicula

#p = Pelicula()
#l = Libro()

#p.Agregar_Pelicula("Rambo", "1:15:00", 26)
#p.Agregar_Pelicula("El Rey León", "1:28:00", 18)
#p.Agregar_Pelicula("Matrix", "2:16:00", 16)
#p.Agregar_Pelicula("Titanic", "3:14:00", 12)
#l.Agregar_Libro("Los hermanos Grin", 210, 23)
#l.Agregar_Libro("Don Quijote de la Mancha", 992, 40)
#l.Agregar_Libro("El nombre del viento", 662, 25)
#l.Agregar_Libro("Cien años de soledad", 368, 30)

def Listar_Stock(numero_stock, obj_p, obej_l):
    lista_productos = []
    nueva_lista = []

    for pel in obj_p.Listar_Peliculas():
        lista_productos.append(pel)

    for lib in obej_l.Listar_Libros():
        lista_productos.append(lib)
        
    for producto in lista_productos:
        if numero_stock >= producto["stock"]:
            nueva_lista.append(producto)
            
    return nueva_lista



#print(Listar_Stock(66))
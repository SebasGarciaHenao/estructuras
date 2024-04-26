class Libro:
    def __init__(self, id, genero, autor, titulo, año_publicacion, tarifa_alquiler):
        self.id_libro = id
        self.genero = genero
        self.autor = autor
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.tarifa_alquiler = tarifa_alquiler
        self.alquilado = False  

    def __str__(self):
        
        return f"id: {self.id_libro}, Género: {self.genero}, Autor: {self.autor}, Título: {self.titulo}, Año: {self.año_publicacion}, Tarifa: {self.tarifa_alquiler}"
    


class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        curr_node = self.head
        while curr_node is not None:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return '\n'.join(result)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def agregar_libro(self, id_libro, genero, autor, titulo, año_publicacion, tarifa_alquiler):
        libro = Libro(id_libro, genero, autor, titulo, año_publicacion, tarifa_alquiler)
        self.append(libro)

  
    def eliminar_libro(self, id_libro):
        if self.head is None:
            return "No existe el libro en la biblioteca"

        if self.head.value.id_libro == id_libro:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return

        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.value.id_libro == id_libro:
                prev_node.next = curr_node.next
                if curr_node == self.tail:
                    self.tail = prev_node
                self.length -= 1
                return
            prev_node = curr_node
            curr_node = curr_node.next
            
    def buscar_por_genero(self, buscar_genero):
        libros_encontrados = []
        for libro in self:
            if libro.value.genero == buscar_genero:
                
                libros_encontrados.append((libro.value))
        if not libros_encontrados:
            print(f"No se encontraron libros del género '{buscar_genero}' disponibles en la biblioteca. ")
        return libros_encontrados

    def buscar_por_titulo(self, buscar_titulo):
        libros_encontrados = []
        for libro in self:
            if libro.value.titulo == buscar_titulo:
               
                libros_encontrados.append(libro.value)
        if not libros_encontrados:
            print(f"No se encontraron libros con el título '{buscar_titulo}' disponibles en la biblioteca. ")
        return libros_encontrados
    
    def buscar_por_autor(self, buscar_autor):
        libros_encontrados = []
        for libro in self:
            if libro.value.autor == buscar_autor:
                
                libros_encontrados.append(libro.value)
        if not libros_encontrados:
            print(f"No se encontraron libros del autor '{buscar_autor}' disponibles en la biblioteca. ")
        return libros_encontrados
    
    def buscar_por_año(self, buscar_año):
        libros_encontrados = []
        for libro in self:
            if libro.value.año_publicacion == buscar_año:
                
                libros_encontrados.append(libro.value)
        if not libros_encontrados:
            print(f"No se encontraron libros del año '{buscar_año}' disponibles en la biblioteca. ")
        return libros_encontrados
    
    def listar_libros_disponibles(self):
         libros_disponibles = []
         for libro in self:
            if not libro.value.alquilado:
                libros_disponibles.append(libro.value)
         if not libros_disponibles:
            print("No hay libros disponibles para alquilar en la biblioteca.")
         else:
            print("Estos son los libros disponibles para alquilar: ")
            for libro in libros_disponibles:
                print(libro)

          
            while True:
                try:
                    id_libro = int(input("Ingrese el número del libro que desea alquilar o ingrese 0 si desea salir: "))
                    if id_libro == 0:
                        break
                    for libro in libros_disponibles:
                        if libro.id_libro == id_libro:
                            libro.alquilado = True
                            print(f"Has alquilado el libro '{libro.titulo}' ")
                   
                        
                except ValueError:
                    print("Ingrese un número válido.")

    def listar_libros_alquilados(self):
        libros_alquilados = []
        for libro in self:
            if libro.value.alquilado:
                libros_alquilados.append(libro.value)
        if not libros_alquilados:
            print("No hay libros alquilados.")
        else:
            print("Libros alquilados:")
            for libro in libros_alquilados:
                print(libro)
                
    def listar_libros_disponibles_por_genero(self, genero):
        libros_disponibles = []
        for libro in self:
            if libro.value.genero == genero and not libro.value.alquilado:
                libros_disponibles.append(libro.value)
        if not libros_disponibles:
            print(f"No hay libros del género '{genero}' disponibles para alquilar en la biblioteca.")
        else:
            print(f"Estos son los  libros disponibles para alquilar del género '{genero}': ")
            for libro in libros_disponibles:
                print(libro)
                
             # Permitir al usuario alquilar un libro
            while True:
                try:
                    id_libro = int(input("Ingrese el número del libro que desea alquilar o ingrese 0 si desea salir: "))
                    if id_libro == 0:
                        break
                    for libro in libros_disponibles:
                        if libro.id_libro == id_libro:
                            libro.alquilado = True
                            print(f"Has alquilado el libro '{libro.genero}' ")
                   
                except ValueError:
                    print("Ingrese un número válido.")
                    
    def listar_libros_alquilados_por_genero(self, genero):
        libros_alquilados = []
        for libro in self:
            if libro.value.genero == genero and libro.value.alquilado:
                libros_alquilados.append(libro.value)
        if not libros_alquilados:
            print(f"No hay libros del género '{genero}'  en la biblioteca.")
        else:
            print(f"Estos son los libros alquilados del género '{genero}':")
            for libro in libros_alquilados:
                print(libro)
                
    def devolver_libro(self, numero_libro):
        for libro in self:
            if libro.value.id_libro == numero_libro and libro.value.alquilado:
                libro.value.alquilado = False
                print(f"Has devuelto el libro '{libro.value.titulo}' ")
                return
        print("No se encontró un libro con ese número o el libro no está alquilado.")

    def aplicar_descuento(self, libros_alquilados):
     if len(libros_alquilados) >= 2:
        total_tarifa_alquiler = sum(libro.tarifa_alquiler for libro in libros_alquilados)
        descuento_total = total_tarifa_alquiler * 0.1
        total_con_descuento = total_tarifa_alquiler - descuento_total

        print("Se aplicó un descuento del 10% a los libros alquilados:")
        for libro in libros_alquilados:
            print(f"Libro '{libro.titulo}': Tarifa de alquiler original: {libro.tarifa_alquiler}, Tarifa diaria con descuento: {libro.tarifa_alquiler - (libro.tarifa_alquiler * 0.1)}")
        print(f"Total a pagar con descuento: {total_con_descuento}")
        
     
    def calcular_ingreso_total(self):
     ingreso_total = 0
     for libro in self:
        if libro.value.alquilado:
            tarifa = libro.value.tarifa_alquiler
                
            if self.contar_libros_alquilados() >= 2:
                descuento = tarifa * 0.1
                tarifa -= descuento
            ingreso_total += tarifa
    
     return ingreso_total
            
           
    
    def contar_libros_alquilados(self):
     contador = 0
     for libro in self:
        if libro.value.alquilado:
            contador += 1
     return contador

    


             

# Ejemplo de uso:
biblioteca = LinkedList()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(1234, "Terror", "George Romero", "Terror en el bosque", 1954, 7500)
biblioteca.agregar_libro(5678, "Terror", "George Romero", "Dead Island", 1970, 7500)
biblioteca.agregar_libro(5830, "Fantasía", "Cris Redfield ", "", 1985, 7000)
biblioteca.agregar_libro(3482, "Ficción", "Ada Wong", "Escape imposible", 1989, 8000)
biblioteca.agregar_libro(9632, "Romance", "Leon S. Kennedy", "Amor imposible", 1996, 6500)
biblioteca.agregar_libro(7608, "Fantasía", "Arnold Schwarzenegger", "Mundo pintado", 1989, 7000)

# Mostrar los libros en la biblioteca
print("Libros en la biblioteca:")
print(biblioteca)


# Buscar todos los libros disponibles para alquilar
print("\n ")
biblioteca.listar_libros_disponibles()

# Buscar todos los libros alquilados
print("\n ")
biblioteca.listar_libros_alquilados()

#Mostrar el ingreso total
print("\n ")
ingreso_total = biblioteca.calcular_ingreso_total()
print(f"Ingreso total por alquileres: {ingreso_total}")

# Obtener la lista de libros alquilados

libros_alquilados = []
for libro_node in biblioteca:
    if libro_node.value.alquilado:
        libros_alquilados.append(libro_node.value)

# Aplicar descuento si se alquilan 2 o más libros
print("\n ")
biblioteca.aplicar_descuento(libros_alquilados)


# # Mostrar los libros disponibles de un género específico
# genero_buscar = "Terror"
# print("\n ")
# biblioteca.listar_libros_disponibles_por_genero(genero_buscar)

# # Mostrar los libros alquilados de un género específico
# genero_alquilar = "Terror"
# print("\n ")
# biblioteca.listar_libros_alquilados_por_genero(genero_alquilar)


# # Buscar libros por género
# buscar_genero = "Romance"
# print("\nLibros encontrados por el género: ", buscar_genero)
# libros_encontrados = biblioteca.buscar_por_genero(buscar_genero)
# for libro in libros_encontrados:
#     print(libro)

# Devolver un libro alquilado
print("\n ")
biblioteca.devolver_libro(1234)
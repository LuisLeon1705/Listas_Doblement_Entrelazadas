from Nodo import Nodo

#Crea la lista enlazada

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    #Funcion para insertar datos en la posicion dada
    
    def insertar(self, dato, posicion=None):
        nuevo_nodo = Nodo(dato)
        
        #En caso de que la lista este vacia se añade el nodo como cabeza
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        #Si la posicion es 0 (Primera posicion) o menor se pone el nodo como primer elemento de la lista
        
        if posicion is None or posicion <= 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        
        posicion_actual = 0
        #Recorre la lista hasta encontrar la posicion deseada o hasta llegar a la ultima posicion
        
        while actual.siguiente is not None and posicion_actual < posicion - 1:
            actual = actual.siguiente
            posicion_actual += 1
            
        #Inserta el nodo en la posicion deseada
        
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        if actual.siguiente:
            actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo

    #Funcion para eliminar Nodos de la lista

    def eliminar(self, nodo):
        """
        Elimina el nodo dado de la lista sin recorrerla dos veces.
        Se asume que Nodo pertenece a la lista.
        """
        if self.cabeza is None or nodo is None:
            return
        
        #Si el Nodo a eliminar no esta en la cabeza
        
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
            
        #Limpiamos los punteros de el Nodo eliminado
        
        nodo.anterior = None
        nodo.siguiente = None

    #Funcion para invertir la lista sin usar listas auxiliares

    def invertir(self):
        actual = self.cabeza
        temporal = None
        while actual is not None:
            
            #Intercambiamos los punteros
            
            temporal = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temporal
            
            #Pasamos al siguiente Nodo (En el orden original)
            
            actual = actual.anterior
            
        #Ajustamos la cabeza de la lista
            
        if temporal is not None:
            self.cabeza = temporal.anterior

    #Funcion que recorre toda la lista para borrar nodos duplicados sin la necesidad de usar estructuras auxiliares

    def eliminar_duplicados(self):
        actual = self.cabeza
        duplicados_eliminados = {}  # Diccionario para guardar la cantidad de duplicados eliminados por valor
        while actual is not None:
            recorredor = actual.siguiente
            while recorredor is not None:
                if recorredor.dato == actual.dato:
                    siguiente_recorredor = recorredor.siguiente
                    duplicados_eliminados[actual.dato] = duplicados_eliminados.get(actual.dato, 0) + 1
                    self.eliminar(recorredor)
                    recorredor = siguiente_recorredor
                else:
                    recorredor = recorredor.siguiente
            actual = actual.siguiente
        return duplicados_eliminados

    #Funcion que busca un valor en la lista y de no encontrarlo retorna -1

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.dato == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    #Funcion para imprimir la lista

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" <-> ".join(elementos))

    #Funcion que genera un menu para que el usuario pueda escoger que hacer

    def menu(self):
        while True:
            print("\nBienvenido al menú de la lista doblemente enlazada")
            print("1 --> Insertar un nuevo nodo")
            print("2 --> Eliminar nodo(s)")
            print("3 --> Invertir el orden de la lista")
            print("4 --> Eliminar nodos duplicados")
            print("5 --> Buscar elemento(s)")
            print("6 --> Mostrar la lista actual")
            print("7 --> Salir del programa")
            opcion = input("Por favor, elige una opción: ")
            if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("Opción inválida. Intenta de nuevo.")
                continue
            if opcion == "1":
                while True:
                    try:
                        dato = int(input("Por favor, ingresa el dato (número entero): "))
                        break
                    except ValueError:
                        print("Dato inválido. Debes ingresar un número entero.")
                posicion_input = input("Indica la posición donde deseas insertar el nodo (déjala vacía para agregar al final): ")
                if posicion_input == "":
                    posicion = None
                else:
                    while True:
                        try:
                            posicion = int(posicion_input)
                            break
                        except ValueError:
                            print("Posición inválida. Asegúrate de ingresar un número entero.")
                            posicion_input = input("Indica la posición donde deseas insertar el nodo (déjala vacía para agregar al final): ")
                self.insertar(dato, posicion)
                print(f"Se ha insertado el nodo con el valor {dato}.")
            elif opcion == "2":
                while True:
                    try:
                        dato = int(input("Por favor, ingresa el valor del nodo que deseas eliminar: "))
                        break
                    except ValueError:
                        print("Valor inválido. Debes ingresar un número entero.")
                nodos_encontrados = []
                posiciones = []
                actual = self.cabeza
                pos = 0
                while actual is not None:
                    if actual.dato == dato:
                        nodos_encontrados.append(actual)
                        posiciones.append(pos)
                    actual = actual.siguiente
                    pos += 1
                if len(nodos_encontrados) == 0:
                    print("No se encontró ningún nodo con ese valor en la lista.")
                elif len(nodos_encontrados) == 1:
                    self.eliminar(nodos_encontrados[0])
                    print(f"Se eliminó el nodo con el valor {dato} en la posición {posiciones[0] + 1}.")
                else:
                    pos_str = ", ".join(map(lambda x: str(x + 1), posiciones))
                    print(f"Se encontraron {len(nodos_encontrados)} nodos con el valor {dato} en las posiciones: {pos_str}.")
                    while True:
                        try:
                            pos_eliminar = int(input("Ingresa la posición específica (empezando en 1) que deseas eliminar: "))
                            pos_eliminar_internal = pos_eliminar - 1
                            if pos_eliminar_internal in posiciones:
                                break
                            else:
                                print("La posición ingresada no corresponde a ningún nodo con ese valor. Intenta de nuevo.")
                        except ValueError:
                            print("Posición inválida. Debes ingresar un número entero.")
                    actual = self.cabeza
                    contador = 0
                    while actual is not None:
                        if contador == pos_eliminar_internal:
                            self.eliminar(actual)
                            print(f"Se eliminó el nodo con el valor {dato} en la posición {pos_eliminar}.")
                            break
                        actual = actual.siguiente
                        contador += 1
            elif opcion == "3":
                self.invertir()
                print("La lista ha sido invertida exitosamente.")
            elif opcion == "4":
                duplicados_info = self.eliminar_duplicados()
                if duplicados_info:
                    for valor, cantidad in duplicados_info.items():
                        print(f"Se eliminaron {cantidad} nodo(s) duplicados con el valor {valor}.")
                else:
                    print("No se encontraron nodos duplicados para eliminar.")
            elif opcion == "5":
                while True:
                    try:
                        dato = int(input("Por favor, ingresa el valor que deseas buscar: "))
                        break
                    except ValueError:
                        print("Valor inválido. Debes ingresar un número entero.")
                posiciones = []
                actual = self.cabeza
                pos = 0
                while actual is not None:
                    if actual.dato == dato:
                        posiciones.append(pos)
                    actual = actual.siguiente
                    pos += 1
                if len(posiciones) == 0:
                    print("El elemento no se encontró en la lista.")
                elif len(posiciones) == 1:
                    print(f"El elemento {dato} se encuentra en la posición {posiciones[0] + 1}.")
                else:
                    pos_str = ", ".join(map(lambda x: str(x + 1), posiciones))
                    print(f"El elemento {dato} se encontró en las posiciones: {pos_str}.")
            elif opcion == "6":
                print("La lista actual es:")
                self.mostrar()
            elif opcion == "7":
                print("Gracias por utilizar el programa. ¡Hasta luego!")
                break

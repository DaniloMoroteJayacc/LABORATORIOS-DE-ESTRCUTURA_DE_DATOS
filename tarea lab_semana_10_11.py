# -*- coding: utf-8 -*-
"""LABORATORIO 10-11 EDD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sANOi-HJEI708MPjBcqlCKXQV1myZv2u

pregunta 02, verificar el tipo de dato de una variable
"""

variable = 3

assert isinstance(variable, int), "La variable no es de tipo entero (int)"

print("La variable es de tipo entero (int)")

"""pregunta 04, asegurar que una lista no este vacia"""

mi_lista = [1,2,3,4]

assert len(mi_lista) > 0, "La lista está vacía"

print("La lista no está vacía")

"""pregunta 06, asegurar que un ciclo while se ejecuta al menos una vez"""

ejecutado_al_menos_una_vez = False

while not ejecutado_al_menos_una_vez:
    print("El ciclo se ha ejecutado al menos una vez")
    ejecutado_al_menos_una_vez = True

assert ejecutado_al_menos_una_vez, "El ciclo no se ejecutó al menos una vez"

print("El ciclo se ejecutó al menos una vez")

"""pregunta 08"""

def producto(a, b):
    return a * b

assert producto (2, 3) == 6, "El producto de 2 y 3 debería ser 6"

assert producto(5, -2) == -10, "El producto de 5 y -2 debería ser -10"

print("Las verificaciones pasaron correctamente.")

"""pregunta 10,funcion buscar nodo en la lista enlazada simple"""

class Nodo:
    def __init__(self, dato):   #constructores
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end =" --> ")
            actual = actual.siguiente
        print("None")

    def longitud (self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        valores_vistos = set()
        valores_vistos.add(self.cabeza.dato)
        actual = self.cabeza

        while actual.siguiente:
            if actual.siguiente.dato in valores_vistos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                valores_vistos.add(actual.siguiente.dato)
                actual = actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(25)
lista.insertar_al_inicio(125)
lista.insertar_al_final(25)
lista.insertar_al_final(35)
lista.insertar_al_final(3)

#lista.mostrar_lista()
#lista.longitud()
nodo_buscado = lista.buscar(20)
if nodo_buscado:
  print("se encontro el nodo buscado")
else:
  print("no se encontro el nodo buscado")

#lista.eliminar_duplicados()
#lista.mostrar_lista()

"""pregunta 12, crear una funcion que devuelva la longitud de una lista enlazada simple

pregunta 14, crea una funcion que elimine los nodos duplicados

LISTAS ENLAZADAS DOBLES
"""

class Nodo:
    def __init__ (self,dato):
      self.dato = dato
      self.siguiente = None
      self.anterior = None

class Lista_Enlazada_Doble:
    def __init__(self):
      self.inicio = None
      self.fin = None

    def esta_vacia(self):
      return self.inicio is None

    def agregar_al_principio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevoNodo
        else:
            nuevoNodo.siguiente = self.inicio
            self.inicio.anterior = nuevoNodo
            self.inicio = nuevoNodo

    def agregar_al_final(self, dato):
        nuevoNodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio =self.fin = nuevoNodo
        else:
          nuevoNodo.anterior = self.inicio
          self.fin.siguiente = nuevoNodo
          self.fin = nuevoNodo

    def eliminar (self,dato):
          actual = self.inicio
          while actual is not None:
              if actual.dato == dato:
                  if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                  else:
                      self.inicio = actual.siguiente

                  if actual.siguiente is not None:
                      actual.siguiente.anterior = actual.anterior
                  else:
                      self.fin = actual.anterior

                  return

    def agregar(self, dato):
        nuevoNodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        else:
            nuevoNodo.anterior = self.fin
            self.fin.siguiente = nuevoNodo
            self.fin = nuevoNodo

    def contar_pares_impares(self):
        nodoActual = self.inicio
        pares = 0
        impares = 0
        while nodoActual is not None:
            if nodoActual.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            nodoActual = nodoActual.siguiente
        return pares, impares

    def insertar_en_posicion(self, dato, posicion):
        nuevoNodo = Nodo(dato)
        if posicion == 1:
            nuevoNodo.siguiente = self.inicio
            self.inicio.anterior = nuevoNodo
            self.inicio = nuevoNodo
        else:
            nodoActual = self.inicio
            contador = 1
            while contador < posicion - 1 and nodoActual is not None:
                nodoActual = nodoActual.siguiente
                contador += 1
            if nodoActual is None:
                print("La lista no tiene la posición especificada.")
                return
            nuevoNodo.siguiente = nodoActual.siguiente
            nuevoNodo.anterior = nodoActual
            if nodoActual.siguiente is not None:
                nodoActual.siguiente.anterior = nuevoNodo
            nodoActual.siguiente = nuevoNodo

    def eliminar_duplicados(self):
        if self.inicio is None:
            return
        nodos_vistos = set()
        nodoActual = self.inicio
        while nodoActual is not None:
            if nodoActual.dato in nodos_vistos:
                nodo_anterior = nodoActual.anterior
                nodo_siguiente = nodoActual.siguiente
                nodo_anterior.siguiente = nodo_siguiente
                if nodo_siguiente is not None:
                    nodo_siguiente.anterior = nodo_anterior
                else:
                    self.ultimo_nodo = nodo_anterior
            else:
                nodos_vistos.add(nodoActual.dato)
            nodoActual = nodoActual.siguiente

    def imprimir_adelante(self):
        nodoActual = self.inicio
        while nodoActual is not None:
            print(nodoActual.dato, end=" ")
            nodoActual = nodoActual.siguiente
        print()

    def imprimir_atras(self):
        nodoActual = self.fin
        while nodoActual is not None:
            print(nodoActual.dato, end=" ")
            nodoActual = nodoActual.anterior
        print()

lista_doble = Lista_Enlazada_Doble()

lista_doble.agregar(1)
lista_doble.agregar(1)
lista_doble.agregar(2)
lista_doble.agregar(3)
lista_doble.agregar(4)
lista_doble.agregar(43)
lista_doble.agregar(43)
lista_doble.agregar(45)
lista_doble.agregar(48)
lista_doble.agregar(8)
lista_doble.agregar(18)
lista_doble.agregar(18)


actual = lista_doble.inicio
while actual is not None:
    print(actual.dato, end =" --> ")
    actual = actual.siguiente
print()
print("--------------------------------------")
pares,impares = lista_doble.contar_pares_impares() #dato par e impar
print("cantidad de nodos pares:",pares)
print("cantidad de nodos pares:",impares)

print("Lista hacia adelante:") #lista hacia adelante
lista_doble.imprimir_adelante()

print("Lista hacia atrás:") #lista hacia atras
lista_doble.imprimir_atras()
print("---------------------------------------------")
lista_doble.insertar_en_posicion(15,3)
print("Lista hacia adelante:") #lista hacia adelante
lista_doble.imprimir_adelante()

print("Lista hacia atrás:") #lista hacia atras
lista_doble.imprimir_atras()
print("---------------------------------------------")


lista_doble.eliminar_duplicados() # Eliminamos duplicados

print("Lista hacia adelante:") # Imprimimos la lista hacia adelante y hacia atrás
lista_doble.imprimir_adelante()
print("Lista hacia atrás:")
lista_doble.imprimir_atras()
print("---------------------------------------------")

class Pila:
    def __init__(self):
        self.items =[]

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self,elemento):
        self.items.append(elemento)

    def desapilar (self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
          print("La pila esta vacia, no se puede desapilar")

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
          print("la pila esta vacia, no hay elementos en la cima")

    def invertir_cadena(cadena):
          pila = Pila()
          for caracter in cadena: # Apilar cada caracter de la cadena en la pila
              pila.apilar(caracter)

          cadena_invertida = ""  # Construir una nueva cadena desapilando los caracteres de la pila
          while not pila.esta_vacia():
                cadena_invertida += pila.desapilar()

          return cadena_invertida

    def ordenar_pila_ascendente(pila):
        pila_auxiliar = Pila()

        while not pila.esta_vacia():
            elemento_actual = pila.desapilar()

            while not pila_auxiliar.esta_vacia() and pila_auxiliar.ver_tope() > elemento_actual:
                pila.apilar(pila_auxiliar.desapilar())

            pila_auxiliar.apilar(elemento_actual)

        while not pila_auxiliar.esta_vacia():
            pila.apilar(pila_auxiliar.desapilar())

    def calcular(expresion):
        pila = Pila()
        operadores = set(['+', '-', '*', '/'])

    for token in expresion.split():
        if token not in operadores:
            pila.apilar(float(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)

    return pila.desapilar()

mi_pila = Pila()
print("la pila esta vacia ?", mi_pila.esta_vacia())

mi_pila.apilar(5)
mi_pila.apilar(15)
mi_pila.apilar(25)
mi_pila.apilar(45)

print("El elemento en la cima de la pila:",mi_pila.cima())

mi_pila.desapilar()
print("pila despues de desapilar un elemento",mi_pila.items)

mi_pila.desapilar()
print("pila despues de desapilar otro elemento",mi_pila.items)

print("---------------------------------------------")
cadena_original = "Franz Danilo"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)

print("---------------------------------------------")

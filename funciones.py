from random import shuffle,choice           #Importamos las funciones necesarias del módulo random

SI = ["si","s","yes","y","1"]       #Constante con los valores de respuestas validas como si

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,               #Diccionario con los valores unicode de las cartas de poker como clave y su valor como valor
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10
}

print("Cartas: {}".format(" ".join(cartas.keys())))     #Imprimimos las cartas por pantalla
print("Valores: {}".format(list(cartas.values())))      #Imprimimos los valores de asociados a cada carta

lista_cartas = list(cartas)       #Transformamos las claves del diccionario en una lista, como las cartas solo se pueden repetir 2 veces, debido a que cogemos 2, no es necesario crear más lista con otros palos, ya que tienen el mismo valor
shuffle(lista_cartas)           #Barajamos la baraja con el comando shuffle
print(lista_cartas)             #Mostramos las cartas totales barajadas en forma de lista por pantalla


def obtener_carta(lista):        #Esta función nos permitirá sacar una carta aleatoria y añadirla a la lista que le pasemos
    carta = choice(lista_cartas)     #Definimos la carta como un elemento aleatorio de lista_cartas gracias a la función choice
    lista.append(carta)             #La añadimos a la lista y le decimos que nos devuelva la lista modificada
    return lista


def mano(mano_persona):     #Con esta función generamos una mano, un conjunto de dos cartas, llamando a la función previamente definida y hacemos que nos devuelva la lista de dos cartas
    carta1_mano=obtener_carta(mano_persona)
    carta2_mano=obtener_carta(carta1_mano)
    return carta2_mano

def mostrar_mano(mano_persona):      #Con esta función hacemos que se muestren las cartas y el valor asociado a dicha carta
    carta1=mano(mano_persona)       #Definimos una variable llamando a la función mano
    carta1_valor=carta1[0]          #Definimos dos variables, las cuales seran la primera y segunda posicion de la lista, siendo esta de 2 elementos
    carta2_valor=carta1[1]
    print("Cartas: {} {} {} {}\nTotal: {}".format(carta1_valor, cartas[carta1_valor],carta2_valor,cartas[carta2_valor],cartas[carta1_valor]+cartas[carta2_valor]))  #Printamos por pantalla las cartas, los valores y el valor total de la mano
    return cartas[carta1_valor]+cartas[carta2_valor] #Nos devuelve el valor de la mano

def jugar_una_vez():    #Definimos la función para jugar una vez
    while True:
        lista_inicial1=[]       #Creamos 2 listas vacias a las cuales asignaremos la mano del jugador y de la banca respectivamente
        lista_inicial2=[]
        mano_jugador=mostrar_mano(lista_inicial1)       #Generamos la mano del jugador y de la banca
        mano_banca=mostrar_mano(lista_inicial2)
        if mano_jugador>mano_banca and mano_jugador<=21:    #Ponemos las condiciones para determinar si se gana o se pierde, una vez satisfecha la condición salimos del bucle
            print("¡Has ganado!")
            break
        elif mano_jugador<=21 and mano_banca>21:
            print("Has ganado")
            break
        elif mano_jugador==mano_banca and mano_jugador<=21:
            print("Empate")
            break
        elif mano_jugador>21 and mano_banca>21:
            print("Empate")
        else:
            print("Game Over")
            break 

def jugar_de_nuevo(cond):       #Con la función jugar_de_nuevo vemos si la respuesta esta dentro de la constante SI definida previamente, devuelve True, en caso de que no lo esté devolverá falso
    try:
        return input(cond).lower() in SI
    except:
        return False

def jugar():        #Con esta función ya podemos ejecutar el juego
    while True:     #Con la función jugar una vez ejecutamos una partida
        jugar_una_vez()
        if jugar_de_nuevo("¿Desea jugar una nueva partida?: ")==False:  #Con este condicional decimos que si jugar de nuevo es false, printamos una despedida y cerramos la función, en caso contrario seguirá repitiendose hasta que decidamos acabarlo
            print("Hasta la próxima")
            return

if __name__ == "__main__":      #Con esto indicamos si se ha ejecutado o exportado el módulo
    print("Se ha ejecutado el módulo")
    jugar()
else:
    print("Se ha importado el módulo")

from random import shuffle,choice

SI = ["si","s","yes","y","1"]

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10
}

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Valores: {}".format(list(cartas.values())))

lista_cartas = list(cartas)*4
shuffle(lista_cartas)
print(lista_cartas)


def obtener_carta(lista):
    carta = choice(lista_cartas)
    lista.append(carta)
    return lista


def mano(mano_persona):
    carta1_mano=obtener_carta(mano_persona)
    carta2_mano=obtener_carta(carta1_mano)
    return carta2_mano

def mostrar_mano(mano_persona):
    carta1=mano(mano_persona)
    carta1_valor=carta1[0]
    carta2_valor=carta1[1]
    print("Cartas: {} {} {} {}\nTotal: {}".format(carta1_valor, cartas[carta1_valor],carta2_valor,cartas[carta2_valor],cartas[carta1_valor]+cartas[carta2_valor]))
    return cartas[carta1_valor]+cartas[carta2_valor]


def jugar_una_vez():
    while True:
        lista_inicial1=[]
        lista_inicial2=[]
        mano_jugador=mostrar_mano(lista_inicial1)
        mano_banca=mostrar_mano(lista_inicial2)
        if mano_jugador>mano_banca and mano_jugador<=21:
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

def jugar_de_nuevo(cond):
    try:
        return input(cond).lower() in SI
    except:
        return False

def jugar():
    while True:
        jugar_una_vez()
        if not jugar_de_nuevo("¿Desea jugar una nueva partida?: "):
            print("Hasta la próxima")
            return

if __name__ == "__main__":
    print("Se ha ejecutado el módulo")
    jugar()
else:
    print("Se ha importado el módulo")

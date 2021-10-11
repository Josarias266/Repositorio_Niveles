import random

def bot():
    ava = random.randint(1,11)
    if ava == 1:
        selectionated = "Chabelo"
    elif ava == 2:
        selectionated = "Tecun Uman"
    elif ava == 3:
        selectionated = "Ricardo Arjona"
    elif ava == 4:
        selectionated = "Gaby Moreno"
    elif ava == 5:
        selectionated = "Connor Mcgregor"
    elif ava == 6:
        selectionated = "Jake Paul"
    elif ava == 7:
        selectionated = "El Bicho"
    elif ava == 8:
        selectionated = "Reina Isabel"
    elif ava == 9:
        selectionated = "Jackie Chan"
    elif ava == 10:
        selectionated = "Jalks"
    elif ava == 11:
        selectionated = "Lucas"
    print("Personaje seleccionado: ", selectionated)

bot()
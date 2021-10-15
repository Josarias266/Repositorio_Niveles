import os
#si punch_1 = patada and 
hp_1 = 10
at_2 = 1
os.system ("cls")
print ("Vida Inicial: ", hp_1)
print ("Ataque: ", at_2)
while hp_1 >= 1:
    hp_1 = hp_1 - at_2
    print ("Vida actual: ", hp_1)
    input ("Pausa...")
print ("Vida Final: ", hp_1)
print ("Bienvenido!")
print ("Escoje un Enemigo de la lista para derrotarlo")
print ("Whomp")
print ("Metapod")
print ("Tohru")
print ("Koopa-Troopa")
print ("Momia")
print ("Zombi")
print ("Spider")
print ("Cuervo")
print ("Farm")
print ("Jalks")

c = input("¿Qué enemigo quieres derrotar?: ")
c = c.upper()
if c == "WHOMP":
 sig = "Whomp"
elif c == "METAPOD":
 sig = "Metapod"
elif c == "TOHRU":
 sig = "Tohru"
elif c == "KOOPA-TROOPA":
 sig = "Koopa-Troopa"
elif c == "MOMIA":
 sig = "Momia"
elif c == "ZOMBI":
 sig = "Zombi"
elif c == "SPIDER":
 sig = "Spider"
elif c == "CUERVO":
 sig = "Cuervo"
elif c == "FARM":
 sig = "Farm"
elif c == "JALKS":
 sig = "Jalks"
else:
 print ("Asegurate de haber escogido un enemigo de la lista y de haberlo escrito bien xD")
 
print ("Felicidades! Has derrotado a " + (sig))
input ("Eso fue todo, presiona la tecla enter para salir...")
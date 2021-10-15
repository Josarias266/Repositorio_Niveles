import os

x = 10
y = 1
os.system ("cls")
print ("Vida Inicial: ", x)
print ("Ataque: ", y)
while x >= 1:
    x = x - y
    print ("Vida actual: ", x)
    input ("Pausa...")
print ("Vida Final: ", x)
print("Ingrese 4 numeros pisitivos enteros: ")
a = int(input('No.1: '))
b = int(input('No.2: '))
c = int(input('No.3: '))
d = int(input('No.4: '))

lista = [a, b, c, d ]
def orden(e):
    e.sort() # ORdena de forma descendente
    e.reverse()# Lo invierte de forma Mayor a menor
    for h in e:
        print("->", h)

orden(lista)
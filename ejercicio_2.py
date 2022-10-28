def relacion(a,b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0

print("Ingrese 2 numeros pisitivos enteros: ")
a = int(input('No.1: '))
b = int(input('No.2: '))
print(relacion(a,b))



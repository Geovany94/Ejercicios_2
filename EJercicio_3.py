
def recortar(munero,minimo,maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

print("Ingrese 3 numeros pisitivos enteros: ")
numero = int(input('Ingrese numero: '))
minimo = int(input('Ingrese minimo: '))
maximo = int(input('Ingrese maximo: '))
print("devolver", recortar(numero,minimo,maximo))


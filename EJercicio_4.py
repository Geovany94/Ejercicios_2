numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
numero3 = int(input('Ingrese el tercer  numero: '))

if numero1 < numero2 and numero1 < numero3:
    mcd = numero1
elif numero2 < numero1 and numero2 < numero3:
    mcd = numero2
else:
    mcd = numero3

while True:
    if numero1 % mcd == 0 and numero2 % mcd == 0 and numero3 % mcd == 0: # el % para obtener el residuo
        print ("El MCD es: ", mcd)
        break
    else:
        mcd -= 1
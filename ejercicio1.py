# Algortimo que lea un numero, si es negativo lo imprima junto con su positivo.

Num = float(input("Digita un número: "))

if Num < 0:

    print ("Número negativo: ", Num)
    print ("Número positivo: ", abs(Num))
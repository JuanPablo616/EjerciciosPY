#capture 3 numeros y diga cuales son mayor menor e igual

Num1 = float(input("Digite el primer número: "))
Num2 = float(input("Digite el segundo número: "))
Num3 = float(input("Digite el tercer número: "))

mayor = max(Num1, Num2, Num3)
menor = min(Num1, Num2, Num3)

if Num1 == Num2 == Num3:
    print("los numeros son iguales.")
elif Num1 != Num2 and Num1 != Num3 and Num2!= Num3:
    print("Los números son diferentes.")
else:
    print("algunos números son iguales.")

print ("El numero mayor es:", mayor)
print("El número menor es:", menor)
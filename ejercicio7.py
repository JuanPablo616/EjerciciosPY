Registro1 = input("Digite su nombre: ")
Registro2 = int(input("Digite su edad: "))
Registro3 = input("Digite su sexo (H/M): ")
Registro4 = input("Digite su estado civil(soltero/casado): ")


if (Registro2 > 40 and Registro3.strip().upper() == "H" and Registro4.strip().lower() == "casado") \
    or(Registro2 < 50 and Registro3.strip().upper() == "M" and Registro4.strip().lower() == "soltera" ) :
    print("el nombre es" ,Registro1)

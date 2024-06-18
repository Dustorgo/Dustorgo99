Nombre=input("Escrib tu nombre: ")

Nota=int(input("Digita tu nota: "))
if Nota <5:
    print("El estudiante",Nombre, "con nota", Nota,"es insuficiente")
elif Nota >=5 and Nota<7:
    print("El estudiante",Nombre, "con nota",Nota,"Es suficiente")
elif Nota >=7 and Nota<9:
    print("El estudiante",Nombre, "con nota",Nota,"Es notable")
elif Nota >=9 and Nota <=10:
    print("El estudiante",Nombre, "con nota",Nota,"Es sobresaliente")

    
print("Sistema de control vacacional \n")

nombre_empleado=input("por favor introduce el nombre del empleado: ")
clave_departamento=int(input("Por favor introduce la clave del departamento:  "))
antiguedad_empleado=float(input("Por favor ingrese su antiguedad: "))


if clave_departamento ==1: #condicional primera decision
    if antiguedad_empleado>=1 and antiguedad_empleado <2:
        print ("El empleado ", nombre_empleado, "tiene derecho a 6 dias de vacaciones")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print("El empleado ", nombre_empleado, "tiene derecho a 14 dias de vacaciones ")
    elif antiguedad_empleado >=7:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 dias de vacaciones")
    else:
        print("El empleado", nombre_empleado,"No tiene derecho a vacaciones")

elif clave_departamento ==2:

    if antiguedad_empleado>=1 and antiguedad_empleado <2:
        print ("El empleado ", nombre_empleado, "tiene derecho a 7 dias de vacaciones")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print("El empleado ", nombre_empleado, "tiene derecho a 15 dias de vacaciones ")
    elif antiguedad_empleado >=7:
        print("El empleado ", nombre_empleado, "tiene derecho a 22 dias de vacaciones")
    else:
        print("El empleado", nombre_empleado,"No tiene derecho a vacaciones")

elif clave_departamento ==3:
    
    if antiguedad_empleado>=1 and antiguedad_empleado <2:
        print ("El empleado ", nombre_empleado, "tiene derecho a 10 dias de vacaciones")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 dias de vacaciones ")
    elif antiguedad_empleado >=7:
        print("El empleado ", nombre_empleado, "tiene derecho a 30 dias de vacaciones")
    else:
        print("El empleado", nombre_empleado,"No tiene derecho a vacaciones")

else: #finaliza condicional de primera desicion
    print("Clave de departamento no existe ")
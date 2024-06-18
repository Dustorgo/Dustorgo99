# Lista de ingredientes

ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]

# Solicitamos al usuario si quiere una pizza vegetariana o no

tipo_pizza = input("¿Quieres una pizza vegetariana o no? (v/n): ")

# Si el usuario quiere una pizza vegetariana

if tipo_pizza == "v":
    # Añadimos los ingredientes a la pizza
    ingredientes = ["Mozzarella", "Tomate", ingredientes_vegetarianos[0]]

# Si el usuario quiere una pizza no vegetariana

else:
    # Añadimos los ingredientes a la pizza
    ingredientes = ["Mozzarella", "Tomate", ingredientes_no_vegetarianos[0]]

# Imprimimos los ingredientes de la pizza

print("Tu pizza tiene los siguientes ingredientes:", ingredientes)

# Indicamos si la pizza es vegetariana o no

if ingredientes[2] in ingredientes_vegetarianos:
    print("Tu pizza es vegetariana.")
else:
    print("Tu pizza no es vegetariana.")


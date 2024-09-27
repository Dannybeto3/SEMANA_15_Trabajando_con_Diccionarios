# Diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Johana Jimenez",
    "edad": 29,
    "ciudad": "Quito",
    "profesion": "Arquitecta"
}

# Accedemos al valor asociado con la clave CIUDAD y lo modificamos
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave valor para "profesión"
informacion_personal["profesion"] = "Doctora"

# Verificar si la clave "telefono" existe caso contrario agregar
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "593 987587363"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)

print(informacion_personal["ciudad"])
print(informacion_personal["telefono"])
print(informacion_personal["profesion"])


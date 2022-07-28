# - No usar la libreria 'asyncio.windows_events', ya que solo funciona en windows. En su lugar puede usar la libreria 'uuid'

import csv
import random

with open ("./libretaDeDirecciones/addresses.csv", "a") as csvfile:
    fieldnames = ["nombre ", "direccion ","telefono ", "fechaRegistro ", "ID " ]
    
    writer = csv.DictWriter (csvfile, fieldnames = fieldnames)
    # Las cabeceras no se deben almacenar cada vez que se ejecuta el programa
    writer.writeheader()
    # No usar input como valores, use variables fuera del weiterow y asigne esas variables como valor, por ejemplo:
    # valor_1 = input(...)
    # valor_2 = input(...)
    # valor_3 = input(...)
    # writer.writerow({
    #     "clave_1": valor_1,
    #     "clave_2": valor_2,
    #     "clave_3": valor_3,
    # })
    # - Mejorar la identacion
    writer.writerow({
                        "nombre ": input("ingrese su nombre:  "),
                        "direccion ": input("ingrese su direccion: "),
                        "telefono ": input("ingrese su telefono:  "),
                        # La fecha de registro se debe crear con la libreria datetime, no debe solicitarsela al usuario
                        "fechaRegistro ": input("ingrese su fechaRegistro: "),
                        # Usar la libreria "uuid" vista en clase para el campo ID
                        "ID ": random.randint(0 , 9999999999999999)
                    })
    
print("datos inseratdos")


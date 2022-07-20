from asyncio.windows_events import INFINITE
import csv
import random

with open ("./libretaDeDirecciones/addresses.csv", "a") as csvfile:
    fieldnames = ["nombre ", "direccion ","telefono ", "fechaRegistro ", "ID " ]
    
    writer = csv.DictWriter (csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({   
                        "nombre ": input("ingrese su nombre:  "),
                        "direccion ": input("ingrese su direccion: "),
                        "telefono ": input("ingrese su telefono:  "),
                        "fechaRegistro ": input("ingrese su fechaRegistro: "),
                        "ID ": random.randint(0 , INFINITE)
                    })
    
print("datos inseratdos")


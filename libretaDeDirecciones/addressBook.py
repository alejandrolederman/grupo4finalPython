import csv
ID = 0

with open ("addresses.csv", "w") as csvfile:
    fieldnames = ["nombre", "direccion","telefono", "fechaRegistro", "ID" ]
    writer = csv.DictWriter (csvfile, fieldnames = fieldnames)
    
    writer.writeheader()
    writer.writerow({   
                        "nombre": input("ingrese su nombre: "),
                        "direccion": input("ingrese su direccion: "),
                        "telefono": input("ingrese su telefono: "),
                        "fechaRegistro": input("ingrese su fechaRegistro: "),
                        "ID": ID + 1
                    })
    
print("datos inseratdos")

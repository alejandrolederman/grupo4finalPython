contador_frases=0
contador_palabras=0
open("phrases.txt", "w").close()            #inicializa el archivo, lo vacia.

flag=True
while flag:
    frase=input("Ingrese una frase o escriba <salir> para salir: ")  # utiliza dos claves para salir, una es 
    if frase=="salir" or frase=="the end":                           # conocida (salir) y la otra es secreta (the end)
        flag=False
    else:     
        contador_frases=contador_frases+1
        contador_palabras=contador_palabras+len(frase.split(" "))
        print("")
        print(f"*** Hasta el momento, Usted ha ingresado {contador_frases} frase/s y el total de palabras acumuladas es de {contador_palabras} ***")
        print("")
        f=open("phrases.txt", "a")     # abre archivo
        f.write(frase)                 # escribe la frase
        f.write('\n')                  # baja una linea
        f.close()                      # cierra el archivo, y asi se repite con cada frase


if contador_frases==0:                                           # si sale del programa sin haber ingresado ninguna frase
    print("Usted eligió salir del programa.")                    # recibe ese mensaje
else:
    print("")
    print("Aquí tiene el listado completo de frases ingresadas:") # cuando sale del programa, PERO despues
    print("")                                                     # de haber cargado frases.
    f = open("phrases.txt", "r")                                  # abre y lee el archivo
    print(f.read())                                               # e imprime el contenido del mismo

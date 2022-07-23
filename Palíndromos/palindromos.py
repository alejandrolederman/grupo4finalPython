# - El programa esta incompleto, el usuario deberia seguir ingresando palabras hasta que ingrese una palabra clave.
#   Ademas, deberia ir mostrando en consola la cantidad de palabras palindromo y no palindromo ingrasadas en cada iteracion
palabra = str(input("ingrese palabra: "))
largoDeLaPalabra= len(palabra)
palabraInvertida=str("")
i =int(largoDeLaPalabra)
while (i>0):
    i=i-1
    palabraInvertida=palabraInvertida+palabra[i]
if(palabra==palabraInvertida):
    print("es palindromo")

else:
    print("no es un palindromo")
# - El programa esta incompleto, el usuario deberia seguir ingresando palabras hasta que ingrese una palabra clave.
#   Ademas, deberia ir mostrando en consola la cantidad de palabras palindromo y no palindromo ingrasadas en cada iteracion

palabra = str(input("ingrese palabra: "))
sonPalindromos = 0
noPalin = 0

while palabra != "aloha" and palabra != "bye":
    
    largoDeLaPalabra= len(palabra)
    palabraInvertida=str("")
    i =int(largoDeLaPalabra)
    
    while (i>0):
        i=i-1
        palabraInvertida=palabraInvertida+palabra[i]
        
    if(palabra==palabraInvertida):
        sonPalindromos = sonPalindromos + 1
        print("es palindromo")
        print ("palindromes totales:", sonPalindromos)
        print ("total de no palindromes: ", noPalin)
        palabra = str(input("ingrese palabra: "))
        
    else:
        print("no es un palindromo ")
        noPalin = noPalin + 1
        print ("palindromes totales:", sonPalindromos)
        print ("total de no palindromes: ", noPalin)
        palabra = str(input("ingrese palabra: "))
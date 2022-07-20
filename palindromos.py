
palabra = str(input("ingrese palabra: "))
largoDeLaPalabra= len(palabra)
palabraInvertida=str("")
i =int(largoDeLaPalabra)
while (i>0):
    i=i-1
    palabraInvertida=palabraInvertida+palabra[i]
if(palabra==palabraInvertida):
    print("es palindromo")
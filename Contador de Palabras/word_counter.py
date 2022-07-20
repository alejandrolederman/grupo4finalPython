import os
notas = open ("./Contador de Palabras/phrases.txt")

frase =input('ingrse una frase: ')

if frase == "abra cadabra" or frase =="show time" or frase =="the end":
    print (" fin del programa")
    
else:
    
    for i in range (len(frase.split(' ')) ):
        notas.write[i]
        
    result = len(frase.split(' '))    
    print(frase.split(' '))

    print("There are " + str(result) + " words.")

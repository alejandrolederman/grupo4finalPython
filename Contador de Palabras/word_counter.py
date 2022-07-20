frase =input('ingrse una frase: ')

if frase == "abra cadabra" or frase =="show time" or frase =="the end":
    print (" fin del programa")
    
else:

    result = len(frase.split(' '))

    print(frase.split(' '))

    print("There are " + str(result) + " words.")

import os
here = os.path.dirname(os.path.abspath(__file__))
notas = os.path.join(here, 'phrases.txt')
archivo=open(notas,"w")

frase =input('ingrse una frase: ')
archivo.writelines([frase, " "])
archivo.close()

frases = 0
palabras = 0
total = 0


while  frase != "abra cadabra" and frase !="show time" and frase !="the end":
    
    frases = frases + 1
    palabras = len(frase.split(' ')) 
    total = total + palabras   
    
    print(frase.split(' '))
    print("en total hay " + str(palabras) + " palabras.")
    print ("cantidad de palabras que se ingresaron:    ", frases)
    print ("total de todas las palabras que se guardaron:   ", total )
    
    frase =input('ingrse una frase: ')
    archivo=open(notas,"a")
    archivo.writelines([frase," "])
    archivo.close()
    
else:
    
    print (" fin del programa")
  

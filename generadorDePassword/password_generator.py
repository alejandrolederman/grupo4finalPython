import string, random


mayus=[]                    # defino las listas de acuerdo a si son mayusculas.
minus=[]                    # minusculas, numericas o de caracteres especiales
numer=[]
espec=[]
lista_deseada=[]            # listado de simbolos elegidos por el usuario

for i in range(65,91):      # crea lista de "mayusculas" de acuerdo a los valores ascii
    mayus.append(chr(i))   

for i in range(97,123):     # crea lista de "minusculas" de acuerdo a los valores ascii
   minus.append(chr(i))

for i in range(48,58):      # crea lista de "numeros" de acuerdo a los valores ascii
    numer.append(chr(i))

for i in range(35,39):      # crea lista de "caracteres especiales" de acuerdo a los valores ascii
    espec.append(chr(i))

espec.append(chr(43))       # agrego los simbolos "+" y "-" a la lista "caracteres especiales" por separado 
espec.append(chr(45))       # ya que los valores ascii no son continuos como para poder incluirlos en el for range


print("¿Qué tipo de caracteres desea combinar para su contraseña?") 
quiere_mayus=input("MAYÚSCULAS (s/n): ")
quiere_minus=input("MINÚSCULAS  (s/n): ")
quiere_numer=input("NÚMEROS (s/n): ")
quiere_espec=input("CARACTERES ESPECIALES (s/n): ")
print("")

if quiere_mayus!="s" and quiere_minus!="s" and quiere_numer!="s" and quiere_espec!="s": # si el usuario NO elige ningun simbolo
    print("Como Usted no ha seleccionado ningún símbolo,")
    print("le generaremos una contraseña automática de 16 caracteres: ")  # organizamos una contraseña automatica de 16 simbolos
    for i in range(0,16):
        lista_deseada=mayus+minus+numer                                 # segun la consigan, esta contraseña automatica NO incluye 
        palabra=random.choice(lista_deseada)                            # caracteres especiales                                
        print(palabra,end="")                                          # el comando end=" " imprime un caracter al lado del otro
                                                                     #dejando, o no, espacio, de acuerdo al espacio entre comillas


else:
    print("")
    longitud=0
    while longitud<8:
            try:                                  # verifico minimo de contrase;a y evitar errores si ingresan letras o decimales.
              longitud=int(input("Ingrese la longitud de su contraseña <mínimo 8 caracteres>: "))
            except: 
              print("No es posible ingresar letras ni números con decimales")
                                              # solo si el usuario eligio algun tipo de simbolo,
    print("")                                                                 # entonces le pedimos la longitud de la contraseña 
    print("Su contraseña es:")
    for i in range(0,longitud):

        if quiere_mayus=="s":
            lista_deseada=lista_deseada+mayus                               # con estos if seleccionamos los simbolos deseados
                                                                            
        if quiere_minus=="s":                                               
            lista_deseada=lista_deseada+minus

        if quiere_numer=="s":
            lista_deseada=lista_deseada+numer

        if quiere_espec=="s":
            lista_deseada=lista_deseada+espec


        palabra=random.choice(lista_deseada)                                # aca se generan los valores random y se van imprimiendo
        print(palabra,end="")

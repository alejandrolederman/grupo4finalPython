lista_si_palin=[]
lista_no_palin=[]
a="str aleatoria"

while a!="salir":
    a=input("Ingrese la palabra o <salir> para salir: ")
    if a=="".join(reversed(a)):
         print("Es Palindrome")
         lista_si_palin.append(a)
        
    else:
            if a=="salir":
             print(f"Usted ingresó {len(lista_si_palin)} palabras palindromes y éste es el listado: {lista_si_palin}")
             print(f"Usted ingresó {len(lista_no_palin)} palabras NO palindromes y éste es el listado: {lista_no_palin}")
        
            else:
             print("No es Palindrome")
             lista_no_palin.append(a)

       
    
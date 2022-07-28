lista_si_palin=[]
lista_no_palin=[]
a="str aleatoria"

while a!="salir":
    a=input("Ingrese la palabra o <salir> para salir: ")
    if a=="".join(reversed(a)):
         print("Es Palindrome")
         print("")
         lista_si_palin.append(a)
        
    else:
            if a=="salir":
             print(f"Usted ingresó {len(lista_si_palin)} palabras palindromes y éste es el listado: {lista_si_palin}")
             print("")
             print(f"Usted ingresó {len(lista_no_palin)} palabras NO palindromes y éste es el listado: {lista_no_palin}")
             print("")
             print(f"El total de palabras ingresadas es de: {len(lista_no_palin)+len(lista_si_palin)}")
            else:
             print("No es Palindrome")
             print("")
             lista_no_palin.append(a)

       
    
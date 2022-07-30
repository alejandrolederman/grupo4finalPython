z=0
while z<=0:
    try:
        z=int(input("Ingrese cant.de números de Fibonacci deseada <mayor que 0> : "))
    
        if z==0:
            print("¡Dije números mayores que cero!")
            print("")
        if z<0:
            print("¡Dije sólo números positivos!")
            print("")  
    
            
    except:
        print("")
        print("No es posible ingresar letras ni números con decimales")    
        print("")
        
        
else:
     a=0
     b=1
     c=1
     for i in range (0,z):
        print(c,end="  ")
        c=a+b
        a=b
        b=c
     
# Lista de ejemplo de la sucesion de Fibonacci 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377…
# para verificar resultados.    
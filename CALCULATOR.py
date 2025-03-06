def  suma(a,b):
    return a+b 

def rest (a,b):
    return a-b

def multi (a,b):
    return a*b

def div (a,b):
    return a/b

def calculadora ():
    
    while True:
        print("SELECCIONA UNA OPERACION:")
        print ("1.-SUMA")
        print ("2.-RESTA")
        print ("3.-MULTIPLICACION")
        print ("4.-DIVISION")
        print("5.-CLOSE")

        option=int(input("INGRESA EL NUMERO SEGUN CORRESPONDA A LA OPERACION QUE DESEAS HACER"))
        
        
        if option in [1,2,3,4]:
         n1=int(input("ingresa el primer numero: "))
         n2=int(input("ingresa el segundo numero: "))

        if option ==1:
         print("El RESULTADO DE LA SUMA ES DE: ", suma(n1,n2))

        elif option ==2:
            print("El RESULTADO DE LA RESTA ES DE: ", rest(n1,n2))

        elif option==3:
            print("El RESULTADO DE LA MULTIPLICACION ES DE: ", multi(n1,n2))

        elif option==4:
            print("El RESULTADO DE LA DIVISION ES DE: ", div(n1,n2))

        else:
            print ("********** MODIFIQUE ESTO JAJAJAJJA **********")
            break
calculadora()
     



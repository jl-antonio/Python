#-- 10. Crear un programa que por medio de recursion calcule la suma de los cuadrados de n numeros. --
def recursion (num, sumNumero=0):
    if(num>=0):
        sumNumero+=num**2
        return recursion(num-1,sumNumero)
    else:
        print sumNumero

x=input("Cantidad ?: ")
recursion(x)
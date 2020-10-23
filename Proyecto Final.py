#Esta biblioteca sirve para que no se despliegue todo de golpe 
import time #Para que no se despliegue todo de golpe 
def nombrecliente(nombre):
    print("¡Hola"+" "+"%s!"%nombre)
#Time es para que haya un tiempo de despliegue cuando se ejecuta el programa
    time.sleep(2)
    print("Este es un programa te ayudará a tener un menú de calidad")
    time.sleep(3)


#cuandoescribe cualquier bebida del menú, sele restará lo que se pague 
def cambio(u1,a):
#la condicion "(A<12)" porque el agua es bebida más barata y cuesta 12 pesos 
    if (a<12):
        print("Lo lamentamos, no te alcanza para nada")
    else:
#el acumulador tiene la función de manter la suma de los gastos del usuario
        acum=0
#se establece un limite al cual el acumulado no puede sobrepasar
        limite1=a-12
        ref = 20
        cer = 25
        agua = 12
        bebida=0
        while  acum <= limite1:
            if u1 == "refresco" or u1 == "Refresco" :
                acum=acum+ref
                bebida=bebida+1
#elif hace que si no se cumple la primera condición, se cumplirá la siguiente     
            elif u1 == "cerveza" or u1 == "Cerveza" :
                acum=acum+cer
                bebida=bebida+1
            elif u1 == "agua" or u1 == "Agua" :
                acum=acum+agua
                bebida=bebida+1
            print("lleva acumulados:", acum, "pesos")
            sino=str(input("¿Quiere otra bebida? coloque (sí) o (no)"))
            if sino == "Sí" or sino == "Si" or sino == "sí" or sino == "si":
                u1= str(input("Escriba la otra bebida que guste."))
            else:
                break
        cambio=a-acum
        print("El precio total de su compra fue: ",bebida, acum, " pesos")
        print("Su cambio total es de: ",cambio," pesos") 
def main():
    print("Bienvenido")
    nombre = input("Escribe tu nombre: ")
    nombrecliente(nombre)
    while True:
        print("Elige tu bebida (nombre)")
#Este es el menú que se le muestra al cliente 
        print("Menú:")
        print("1. refreso 20 pesos")
        print("2. cerveza 25 pesos")
        print("3. agua 12 pesos")
#El usuario nos escribirá la bebida  para poder obtener su precio
        u1 = input()
# se calcula el cambio que se le devolverá si es el caso
        print("Inserte la cantidad con la que usted va a pagar")
        a = int(input())
        cambio(u1,a)
#colocará la opción de repetir con el while true y con conti
        conti=str(input("¿Volver a realizar otra compra?, coloque (sí) (no)?"))
        if conti == "No" or conti == "no" or conti == "N" or conti == "n":
            print("Gracias por su tiempo")
            break
main()
#Se vuelve a usar la nueva biblioteca digital
time.sleep(2)       
print ("Escribe las bebidas que deseas que salgan proximamente:")
#Esta lista funciona para guardar los datos ingresados por el usuario
lista= []
tamano=int(input("coloca el número de bebidas sugeridas"))
for i in range(0,tamano):
    nobebs = str(input("Escribe el nombre de las bebidas: "))
    lista.insert(i, nobebs)
print("Nos daría mucho tener en el menú estas bebidas: ", lista)
print ("Vuelva pronto")


print ("Si resuelves las adivinanzas, en la siguiente visita tienes descuento")
print ("Fui por él y nunca lo traje, ¿Qué es?")
print ("Nazco sin padre y al morir nace mi madre, ¿Quién soy?")
#La matriz sirve para guardar información de varias listas
m=[["A","Despensa","Batman"],["B","Cigarros","Gallina"],["C","Camino","Nieve"]]
print("Opciones:")
for x in range(0,len(m)):
#X es un contador que nos sirve para la secuencia de las listas 
    print(m[x][0]," ) " ,m[x][1], " y " ,m[x][2])
r=str(input("\nColoca la letra de la opción correcta (MAYUSCULA)"))
if r == "C" or r== "c":
    print("Respuesta correcta")
else:
    print("Respuesta incorrecta, la respuesta correcta era la opción C")








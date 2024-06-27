
titulos=[]
autores=[]
generos=[]
precios=[]
Ventas=[]
def registrar():
    a=input("escriba el titulo del libro: ")
    titulos.append(a)
    b=input("escriba el autor del libro: ")
    autores.append(b)
    c=input("escriba el Genero del libro: ")
    generos.append(c)
    d=input("ingrese el precio del libro: ")
    precios.append(d)

def Venta():
        Ti=input("¿Cuál es el nombre del Libro? ")
        Co=int(input("¿Cuantas copias se van a vender? "))
        Pu=int(input("¿Cual es el precio del libro? "))
        Pf=Pu*Co
        print("~~~Boleta~~~")
        print()
        print(Ti,": ",Pu," x",Co )
        print("Precio total: ",Pf)
        print()
        print("~~~~~~~~~~~~")
        Ventas.append(Ti)

print ("Bienvendo al sistema de la librería")

while True:
    print("¿Qué desea hacer?")
    print("[1] Registrar libro")
    print("[2] Listar todos los libros")
    print("[3] Registrar venta")
    print("[4] Imprimir reporte de ventas")
    print("[5] Generar txt")
    print("[6] Salir del Programa")

    opción=int(input("Seleccione una opción: "))

    if opción==1:
        print("Registrar libro")
        registrar()

    elif opción==2:
        print("Listar todos los libros")
        print(titulos)
        print(autores)
        print(generos)
        print(precios) 

    elif opción==3:
        print ("Registrar venta")
        Venta()

    elif opción==4:
        print ("imprimir reporte de venta")
        print (Ventas)
    elif opción==5:
        print ("Generar TXT")
        
    elif opción==6:
        print("Saliendo . . . .")
        break
    else:
        print("Seleccione una opción valida")
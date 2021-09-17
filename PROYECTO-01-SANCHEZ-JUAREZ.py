"""
----------------------------------------------------------------------
Proyecto 1. Introducción a Python

Autor:     Sergio Alejandro Sánchez Juárez
Fecha:     16 de septiembre de 2021
----------------------------------------------------------------------
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

print("\n\n*** LifeStore ***\n\n")

#[[nombre de usuario,contraseña]]
admins=[["Javier","J123"],["Sergio","S123"]]

es_admin=0 # 1 Si es admin, 0 No es admin
intentos=1

#Se ejecuta mientras no son más de 2 intentos para el Login y no haya coincidencias en los datos.
while es_admin != 1 and intentos <= 2:
    print("Intento "+str(intentos)+" de 2")
    usuario=input("Ingrese un nombre de usuario: ")
    contraseña=input("Ingrese una contraseña: ")

    for admin in admins:
        if usuario == admin[0] and contraseña == admin[1]:
            es_admin=1
            break
  
    if es_admin==0:
        print("Los datos proporcionados son incorrectos\n")
        intentos+=1

if es_admin==1: #Es admin da bienvenida y muestra menú
    
    print("\n¡ Bienvenido !")
    
    opcion="0" #almacena la opcion del menu elegida
    
    while opcion != "5": #Se ejecuta mientras el usuario no quiera salir del sistema

        menu="""
        \nAnálisis
        1. Productos más vendidos
        2. Productos rezagados
        3. Productos por reseña en el servicio
        4. Ingresos y ventas mensuales
        5. Salir
        """
        print(menu)
        opcion=input("Selecciona una opción (1-5): ")

        if opcion == "1":
            print("\nProductos más vendidos")

            #Listado donde se contabilizan las ventas de los productos
            ventas_productos=[] #nombre producto, ventas totales
            cont=0 #contador de ventas
            
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0] == venta[1]:
                        cont+=1
                if cont!=0:
                    ventas_productos.append([producto[1],cont])
                    cont=0
            
            #Listado donde se contabilizan las búsquedas de los productos
            busquedas_productos=[] #nombre producto, búsquedas totales
            cont=0 #contador de búsquedas
            
            for producto in lifestore_products:
                for busqueda in lifestore_searches:
                    if producto[0] == busqueda[1]:
                        cont+=1
                if cont!=0:
                    busquedas_productos.append([producto[1],cont])
                    cont=0
            
            #Ordenamiento descendente del listado ventas_productos
            ventas_productos.sort(key=lambda x:x[1], reverse=True)

            #Mostrar top 15 de productos con mayores ventas
            print("\nTop 15 de productos con mayores ventas\n")
            
            for i in range(0,15):
                print(str(i+1)+". ("+str(ventas_productos[i][1])+") ventas  "+ventas_productos[i][0])

            #Ordenamiento descendente del listado busquedas_productos
            busquedas_productos.sort(key=lambda x:x[1], reverse=True)

            #Mostrar listado de productos con mayores busquedas
            print("\nListado de 20 productos con mayores búsquedas.\n")
            
            for i in range(0,20):
                print(str(i+1)+". ("+str(busquedas_productos[i][1])+") busquedas  "+busquedas_productos[i][0])

        elif opcion == "2":
            
            print("\nProductos rezagados")

            print("\nProductos con menores ventas")

            #Listado de categorias 
            categorias=[] #nombre de la categoria
            categoria="" #categoria actual
            
            for producto in lifestore_products:
                if categoria != producto[3]:
                    categorias.append(producto[3])
                    categoria=producto[3]
            
            #Listado donde se contabilizan las ventas de los productos
            ventas_productos=[] #nombre del producto, categoria y ventas totales.
            cont=0 #contador de ventas
            
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0] == venta[1]:
                        cont+=1
                
                ventas_productos.append([producto[1],producto[3],cont])
                cont=0
            
            #Ordenamiento ascendente del listado ventas_productos 
            ventas_productos.sort(key=lambda x:x[2])
            
            #Muestra 5 productos por categoria de los menos vendidos
            for categoria in categorias:
                indice=0
                print("\n"+categoria)
                for venta in ventas_productos:
                    if categoria == venta[1]:
                        if indice < 5:
                            print(str(indice+1)+". ("+str(venta[2])+") ventas "+venta[0])
                            indice+=1    
            
            print("\n\nProductos con menores búsquedas")

            #Listado donde se contabilizan las búsquedas de los productos
            busquedas_productos=[] #nombre del producto, categoria y busquedas totales
            cont=0 #contador de busquedas
            
            for producto in lifestore_products:
                for busqueda in lifestore_searches:
                    if producto[0] == busqueda[1]:
                        cont+=1
                busquedas_productos.append([producto[1],producto[3],cont])
                cont=0
            
            #Ordenamiento ascendente del listado busquedas_productos 
            busquedas_productos.sort(key=lambda x:x[2])

            #Muestra 7 productos por categoria de los menos buscados
            for categoria in categorias:
                indice=0
                print("\n"+categoria)
                for busqueda in busquedas_productos:
                    if categoria == busqueda[1]:
                        if indice < 7:
                            print(str(indice+1)+". ("+str(busqueda[2])+") busquedas "+busqueda[0])
                            indice+=1 

        elif opcion == "3":
            
            print("\nProductos por reseña en el servicio")

            #Listado donde se almacenan las reseñas de los productos con promedios de valoración y promedios de devoluciones de los totales de venta de cada producto
            
            reseñas_productos=[] #nombre del producto, promedio de valoración, promedio de devoluciones
            cont=0 #contador de ventas
            score=0 # almacena sumatoria de valoraciones
            refund=0 # almacena sumatoria de devoluciones
            
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0] == venta[1]:
                        cont+=1
                        score+=venta[2]
                        refund+=venta[4]
                if cont!=0: #Si hay ventas del producto en cuestión
                    prom_score=score/cont #promedio de valoraciones

                    if refund !=0: #Si hubo devoluciones obtiene promedio, si no otorga el 0
                        prom_refund=refund/cont #promedio de devoluciones
                    else:
                        prom_refund=0
                    
                    reseñas_productos.append([producto[1],prom_score,prom_refund])
                    cont=0
                    score=0
                    refund=0
            
            #Ordenamiento descendente del listado reseñas_productos 
            reseñas_productos.sort(key=lambda x:x[1], reverse=True)
            
            print("\nListado de los productos con las mejores reseñas")

            #Muestra listado de los productos con las mejores reseñas
            indice=0
            for reseña in reseñas_productos:
                if reseña[1]>=5.0:
                    print(str(indice+1)+". ("+str(reseña[1])+") score "+reseña[0])
                    indice+=1 
            
            print("\n\nListado de los productos con las peores reseñas")

            #Muestra listado de los productos con las peores reseñas
            indice=0
            longitud=len(reseñas_productos)
            for i in range(longitud-1,0,-1):
                if reseñas_productos[i][1]<=3.0:
                    print(str(indice+1)+". ("+str(reseñas_productos[i][1])+") score "+reseñas_productos[i][0])
                    indice+=1 

        elif opcion == "4":
            print("\nIngresos y ventas mensuales")

            ventas=[] #fecha, precio
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0] == venta[1]:
                        ventas.append([venta[3],producto[2]])

            ventas_mensuales=[] #mes, ganancias
            total=0 #almacena sumatoria de ventas por cada vez
            total_ingresos=0 #ingresos totales por las ventas
            for i in range(1,13):
                for venta in ventas:
                    if int(venta[0][3:5]) == i:
                        total+=venta[1]
                        total_ingresos+=venta[1]
                ventas_mensuales.append([i,total])
                total=0
            
            print("\nTotal de ingresos: "+str(total_ingresos)+" pesos.")
            print("\nPromedio de ventas mensuales: "+str(total_ingresos/12)+" pesos")
            
            #Ordenamiento descendente de las ventas mensuales 
            ventas_mensuales.sort(key=lambda x:x[1], reverse=True)

            print("\nMeses con mayores ventas: ")

            #Listado de los meses del año
            #num de mes, mes
            meses=[[1,"Enero"],[2,"Febrero"],[3,"Marzo"],[4,"Abril"],[5,"Mayo"],[6,"Junio"],[7,"Julio"],[8,"Agosto"],[9,"Septiembre"],[10,"Octubre"],[11,"Noviembre"],[12,"Diciembre"]]

            #Muestra listado de los meses con las mejores ventas
            for i in range(0,5):
                for mes in meses:
                    if ventas_mensuales[i][0]==mes[0]:
                        print(str(i+1)+". "+mes[1]+" "+str(ventas_mensuales[i][1])+" pesos.") 

        elif opcion == "5":
            print("\nRealizado por: Sergio Alejandro Sánchez Juárez\n")
        else:
            print("\nPor favor, ingrese un número del 1 al 5.\n")

else: #Si no es admin, muestra el msj en consola y sale del sistema.
    print("Lo siento. No es un administrador.\n")
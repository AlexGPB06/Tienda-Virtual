# Alejandro Garcia Pelayo Banda  21/09/2024
# Este programa es sobre el Menu principal de nuestro negocio donde se solicita el nombre del empleado,las 5 opciones del menu principal , se dara en la opcion 1
# el orden de los produtos con sus categoria y notas, donde al final de podra imprimir la nota y el monto total de los productos
import csv #Se importa la libreria csv para obtener sus funciones

Monto = [] #Creamos una lista dobde se acumulara el ponto
lista = [] #Hacemos una lista donde ira las categorias de los productos
precio = []#Hacemos una lista donde se guardara los precios de los productos
inventario = []#Se crea una lista para guardar los datos del inventarii
lista_productos = [] #Se crea uba lista para guardar los datos de los productos

with open("invetnario.csv","r") as csvfile: # Abrimos el archivo csv como read
      reader = csv.reader(csvfile,delimiter=',') #hacemos que lea el archivo y lo separamos con comas los datos
      for line in reader: #creamos un cuclo for para cada elemneto del archivo
            inventario.append(line) #Guardamos lso elementos del archivo en la lista de inventario
csvfile.close() #se cierra el archivo para evitar alguna corrupcion

def menu_cpu():# Definimos la funcion para las opciones de de ordenar lista
    contador = 0 #se crea un contador desde 0
    while contador == 0: #se crea un ciclo solo si el contador es igual a 0
      try:  #ponemos un try para que nos marque e impirma el error #ponemos un try para que nos marque e impirma el error
            lista_productos = ["CPU"] #Se asigna el tipo de producto en la lista
            pregunta = int(input("\n1)Intel \n2)AMD\nPresione el numero de la marca que desee: ")) #Asiganmos que la variable pregunta sea el numero de la marca que desee el usuario
            if pregunta == 1: #Si la pregunta vale 1 hara lo siguiente
                  Intel = "Intel"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                  lista_productos.append(Intel)#Agregamos la marca a la lista de productos que creamos
                  productosintel = ["Intel Core i9" , "$",  15000 , "Intel Core i7" , "$", 8000 , "Intel Core i5", "$",5000]#Asiganmos una lista de productos donde se guardara en una lista
                        #                       0      1     2           3           4    5        6             7    8
                  while contador == 0: #se crea un while true
                        try:  #ponemos un try para que nos marque e impirma el error #ponemos un try para que nos marque e impirma el error
                              while True: #se crea un while true 
                                    print("\n Los productos son:\n 1.) Intel Core i9 - $15000 \n 2.) Intel Core i7 - $8000 \n 3.) Intel Core i5 - $5000 \n")#Imprimimos la lista de productos con el presio
                                    preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                    if preguntados >= 4 or preguntados <= 0: #se crea un if para excluir numeros mayores y menores
                                          print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                    else: #se hace para que continue el ciclo
                                          while contador == 0: #ponemos otro ciclo solo si el contador es igual a 0
                                                try:  #ponemos un try para que nos marque e impirma el error #ponemos un try para que nos marque e impirma el error
                                                      print("El inventario actual de",inventario[0][0],"\nson:",inventario[1][0]) #impimimos el invenario con el nombre y cantidad
                                                      if int(inventario[1][0]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                            print('''No tenemos inventario de aquel producto\npresione "0" para salir''') #se imprime lo que debe de hacer el usuario
                                                            salir = int(input(" ")) # ponemos un imput para que el usuario pueda escribir
                                                            if salir == 0: #si el usuario presiona 0 se hara lo siguiente
                                                                  contador += 1 # se le suma al contador y se rompe los 2 ciclo while igual 0
                                                                  break #ponemos un break para romper el ciclo. # se hace un break #ponemos un break para romper el ciclo. para salir
                                                            else: # si presiona otro numero se hara lo siguiente
                                                                  print("presione 0") #se imprime la siguente instruccion
                                                                  continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                      pregunta_inventario = int(input("Cuantos CPU va a querer? ")) #se pregunta la cantidad de producto que va a querer el usuario
                                                      if pregunta_inventario > int(inventario[1][0]) or pregunta_inventario < 0 : #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                            1/0 #Se crea una division de un numero entre 0 para que marque un error y evite el proceso

                                                      elif pregunta_inventario <= int(inventario[1][0]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                            inventario[1][0] = int(inventario[1][0]) - pregunta_inventario #se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                      if preguntados ==1 :# si el usuario selecciona 1 se hara lo siguiente
                                                            lista_productos.append(productosintel[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                            lista_productos.append(pregunta_inventario) #se agrega a la lista el numero cantidad
                                                            lista_productos.append(productosintel[2]) #se agrega a la lista el precio
                                                            lista_productos.append(productosintel[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                            precio.append(productosintel[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                            lista.append(lista_productos) # Se agrega la lista la lista de productos
                                                            print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosintel[0] ,"$",productosintel[2],"c/u","Total:",productosintel[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                            contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                            break #ponemos un break para romper el ciclo. #ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                      elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                            lista_productos.append(productosintel[3])#Se agregara a la lista el indice 3 que es el nombre del producto
                                                            lista_productos.append(pregunta_inventario)#se agrega a la lista el numero cantidad
                                                            lista_productos.append(productosintel[5]) #se agrega a la lista el precio
                                                            lista_productos.append(productosintel[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                            precio.append(productosintel[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                            lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                            print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosintel[3] ,"$",productosintel[5],"c/u","Total:",productosintel[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                            contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                            break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                      elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                            lista_productos.append(productosintel[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                            lista_productos.append(pregunta_inventario)#se agrega a la lista el numero cantidad
                                                            lista_productos.append(productosintel[8]) #se agrega a la lista el precio
                                                            lista_productos.append(productosintel[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                            precio.append(productosintel[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                            lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                            print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosintel[6] ,"$",productosintel[8],"c/u","Total:",productosintel[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                            contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                            break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                      else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                            print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                      print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                      print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")      #se imprime lo siguiente
                                    break #ponemos un break para romper el ciclo. # se rompe el ciclo
                        except ValueError: #ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                              print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                      
            elif pregunta == 2 : #si el usuario selecciona 1 se hara lo siguiente
                  while contador == 0:#se crea un ciclo solo si el contador es igual a 0
                        try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                              lista_productos = ["CPU"]#Se asigna el tipo de producto en la lista
                              AMD = "AMD"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                              lista_productos.append(AMD)##Agregamos la marca a la lista de productos que creamos
                              print("\nLos productos son:\n 1.) AMD Ryzen 9 - $1500 \n 2.) AMD Ryzen 7 - $8000 \n 3.) AMD Ryzen 3 - $5000 \n")#Imprimimos la lista de productos con el presio
                              productosAMD = ["AMD Ryzen 9" , "$",  15000 , "AMD Ryzen 7" , "$", 8000 , "AMD Ryzen 3", "$", 5000]#Asiganmos una lista de productos donde se guardara en una lista
                                    #                    0            1     2           3           4    5        6          7    8
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    while True: # se crea un while true 
                                          preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                          if preguntados >= 4 or preguntados <= 0: #se crea un if para excluir valores mayores y menores
                                                print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                          else: # se usa para seguir con el ciclo
                                                while contador == 0: #ponemos otro ciclo solo si el contador es igual a 0
                                                      try:  #ponemos un try para que nos marque e impirma el error #
                                                            print("El inventario actual de",inventario[0][0],"\nson:",inventario[1][0])#imprimimos el invenario con el nombre y cantidad
                                                            if int(inventario[1][0]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                  print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                  salir = int(input("Ingrese aqui el número 0: ")) # ponemos un imput para que el usuario pueda escribir
                                                                  if salir == 0:  #si el usuario presiona 0 se hara lo siguiente
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo 
                                                                  else:# si presiona otro numero se hara lo siguiente
                                                                        print("presione 0")  #se imprime la siguente instruccion
                                                                        continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                            pregunta_inventario = int(input("Cuantos CPU va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                            if pregunta_inventario > int(inventario[1][0]) or pregunta_inventario < 0 :  #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                  1/0 #Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                            elif pregunta_inventario <= int(inventario[1][0]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                  inventario[1][0] = int(inventario[1][0]) - pregunta_inventario #se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                            if preguntados ==1 :## si el usuario selecciona 1 se hara lo siguiente
                                                                              lista_productos.append(productosAMD[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                              lista_productos.append(pregunta_inventario) #se agrega a la lista el numero cantidad
                                                                              lista_productos.append(productosAMD[2]) #se agrega a la lista el precio
                                                                              lista_productos.append(productosAMD[2]*pregunta_inventario) #Se guarda el valor total
                                                                              precio.append(productosAMD[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                              lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                              print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[0] ,"$",productosAMD[2],"c/u","Total:",productosAMD[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                              lista_productos.append(productosAMD[3])#)#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                              lista_productos.append(pregunta_inventario) #se agrega a la lista el numero cantidad
                                                                              lista_productos.append(productosAMD[5]) #se agrega a la lista el precio
                                                                              lista_productos.append(productosAMD[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                              precio.append(productosAMD[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                              lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                              print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[3] ,"$",productosAMD[5],"c/u","Total:",productosAMD[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                              lista_productos.append(productosAMD[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                              lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                              lista_productos.append(productosAMD[8]) #se agrega a la lista el precio
                                                                              lista_productos.append(productosAMD[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                              precio.append(productosAMD[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                              lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                              print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[6] ,"$",productosAMD[8],"c/u","Total:",productosAMD[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                              print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                      except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                            print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                      except ValueError:
                                                            print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                          break #ponemos un break para romper el ciclo.                              
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                    
                        except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas#se imprime lo siguiente
                              print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
            else:#Si el usuario pone algo erroneo se hara lo siguiente
                  print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
      except ValueError:
            print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente

def menu_motherboard():# Definimos la funcion para las opciones de de ordenar lista
      contador = 0#se crea un contador desde 0
      while contador == 0:#se crea un ciclo solo si el contador es igual a 0
            try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                  lista_productos = ["Motherboard"]#Se asigna el tipo de producto en la lista
                  pregunta = int(input("1)Intel\n2)AMD\nPresione el numero de la marca que desee: "))#hacemos la pregunta sobre la primera categoria que son las marcas
                  if pregunta == 1:#Si el ususario escribio bien la primera marca se hara lo siguiente 
                        Intel = "Intel"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                        lista_productos.append(Intel)#Agregamos la marca a la lista de productos que creamos
                        productosIntel = ["Z790" , "$",  6000 , "Z690" , "$", 4000 , "B560", "$", 2000]#Asiganmos una lista de productos donde se guardara en una lista
                              #                    0            1     2           3           4    5        6          7    8
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    while True:
                                          print("\nLos productos son:\n 1.) Z790 - $6000 \n 2.) Z690 - $4000 \n 3.) B560 - $2000 \n")#Imprimimos la lista de productos con el presio
                                          preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                          if preguntados >= 4 or preguntados <= 0: #ponemos un if para exccluir valores mayores y menores
                                                print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                          else: #else para que siga el ciclo
                                                while contador == 0: #se crea un contador while para tener un ciclo en el try
                                                      try:  #ponemos un try para que nos marque e impirma el error
                                                            print("El inventario actual de",inventario[0][1],"\nson:",inventario[1][1])#imprimimos el invenario con el nombre y cantidad
                                                            if int(inventario[1][1]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                  print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                  salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                  if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:# si presiona otro numero se hara lo siguiente
                                                                        print("presione 0") #se imprime la siguente instruccion
                                                                        continue# se pone continue para que vuelva a repetir el proceso desde el if
                                                            pregunta_inventario = int(input("Cuantos Motherboard va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                            if pregunta_inventario > int(inventario[1][1]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                  1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                            elif pregunta_inventario <= int(inventario[1][1]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                  inventario[1][1] = int(inventario[1][1]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                            if preguntados ==1 :# si el usuario selecciona 1 se hara lo siguiente
                                                                              lista_productos.append(productosIntel[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                              lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                              lista_productos.append(productosIntel[2]) #se agrega a la lista el precio
                                                                              lista_productos.append(productosIntel[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio                                                                           
                                                                              precio.append(productosIntel[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                              lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                              print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosIntel[0] ,"$",productosIntel[2],"c/u","Total:",productosIntel[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo. #ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                              lista_productos.append(productosIntel[3])#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                              lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                              lista_productos.append(productosIntel[5]) #se agrega a la lista el precio
                                                                              lista_productos.append(productosIntel[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                              precio.append(productosIntel[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                              lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                              print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosIntel[3] ,"$",productosIntel[5],"c/u","Total:",productosIntel[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo. #ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                              lista_productos.append(productosIntel[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                              lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                              lista_productos.append(productosIntel[8])#se agrega a la lista el precio
                                                                              lista_productos.append(productosIntel[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                              precio.append(productosIntel[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                              lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                              print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosIntel[6] ,"$",productosIntel[8],"c/u","Total:",productosIntel[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------") # Se imprime el producto y el precio que eligio el usuario
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo. #ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                              print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                      except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                            print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                      except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                            print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                          break #ponemos un break para romper el ciclo.
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                              
                  elif pregunta == 2:#Si el ususario escribio bien la segunda marca se hara lo siguiente 
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    lista_productos = ["Motherboard"]#Se asigna el tipo de producto en la lista
                                    AMD = "AMD"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                                    lista_productos.append(AMD)##Agregamos la marca a la lista de productos que creamos
                                    print("\nLos productos son:\n 1.) B650 - $7000 \n 2.) B550 - $5000 \n 3.) B520 - $3000 \n")#Imprimimos la lista de productos con el presio
                                    productosAMD = ["B650" , "$",  7000 , "B550" , "$", 5000 , "B520", "$", 3000]#Asiganmos una lista de productos donde se guardara en una lista
                                          #                    0            1     2           3           4    5        6          7    8
                                    try:  #ponemos un try para que nos marque e impirma el error
                                          while True: # se crea un ciclo
                                                preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                                if preguntados >= 4 or preguntados <= 0: #if para excluir valores mayores y menores
                                                      print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                                else: #else para que siga el ciclo del try
                                                      while contador == 0: #para tener otro ciclo para el try
                                                            try:  #ponemos un try para que nos marque e impirma el error
                                                                  print("El inventario actual de",inventario[0][1],"\nson:",inventario[1][1])#imprimimos el invenario con el nombre y cantidad
                                                                  if int(inventario[1][1]) == 0:
                                                                        print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                        salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                        if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                        else:# si presiona otro numero se hara lo siguiente
                                                                              print("presione 0") #se imprime la siguente instruccion
                                                                              continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                                  pregunta_inventario = int(input("Cuantos Motherboard va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                                  if pregunta_inventario > int(inventario[1][1]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                        1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                                  elif pregunta_inventario <= int(inventario[1][1]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                        inventario[1][1] = int(inventario[1][1]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                                  if preguntados ==1 :## si el usuario selecciona 1 se hara lo siguiente
                                                                        lista_productos.append(productosAMD[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                        lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                        lista_productos.append(productosAMD[2])#se agrega a la lista el precio
                                                                        lista_productos.append(productosAMD[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                        precio.append(productosAMD[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                        lista.append(lista_productos)# Se agrega la lista la lista de productos 
                                                                        print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[0] ,"$",productosAMD[2],"c/u","Total:",productosAMD[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                        lista_productos.append(productosAMD[3])#)#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                        lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                        lista_productos.append(productosAMD[5])#se agrega a la lista el precio
                                                                        lista_productos.append(productosAMD[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                        precio.append(productosAMD[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                        lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                        print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[3] ,"$",productosAMD[5],"c/u","Total:",productosAMD[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                        lista_productos.append(productosAMD[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                        lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                        lista_productos.append(productosAMD[8])#se agrega a la lista el precio
                                                                        lista_productos.append(productosAMD[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                        precio.append(productosAMD[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                        lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                        print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[6] ,"$",productosAMD[8],"c/u","Total:",productosAMD[6]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                        print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                            except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                            except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                                  print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                break #ponemos un break para romper el ciclo.
                                    except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                          print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                        print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
            except ValueError: 
                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")       #se imprime lo siguiente                                  

def menu_ram():# Definimos la funcion para las opciones de de ordenar lista
      contador = 0#se crea un contador desde 0
      while contador == 0:#se crea un ciclo solo si el contador es igual a 0
            try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                  lista_productos = ["RAM"]#Se asigna el tipo de producto en la lista
                  pregunta = int(input("1)Corsair\n2)Kingston\nPresione el numero de la marca que desee: "))#hacemos la pregunta sobre la primera categoria que son las marcas
                  if pregunta == 1:#Si el ususario escribio bien la primera marca se hara lo siguiente 
                        Corsair = "Corsair"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                        lista_productos.append(Corsair)#Agregamos la marca a la lista de productos que creamos
                        productosCorsair = ["Corsair 8 Ram" , "$",  600 , "Corsair 16 Ram" , "$", 15000 , "Corsair 32 Ram", "$", 3500]#Asiganmos una lista de productos donde se guardara en una lista
                        #                    0            1     2           3           4    5        6          7    8
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    while True: #se crea un ciclo while para el try
                                          print("\nLos productos son:\n 1.) Corsair 8 Ram - 600 \n 2.) Corsair 16 Ram - $15000 \n 3.) Corsair 32 Ram - $3500 \n")#Imprimimos la lista de productos con el presio
                                          preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                          if preguntados >= 4 or preguntados <= 0: #para excluir valores mayores y menores
                                                print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                          else: #para continuar por el ciclo
                                                while contador == 0: #para que el try siga en ciclo
                                                      try:  #ponemos un try para que nos marque e impirma el error
                                                            print("El inventario actual de",inventario[0][2],"\nson:",inventario[1][2])#imprimimos el invenario con el nombre y cantidad
                                                            if int(inventario[1][2]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                  print('''No tenemos inventario de aquel producto\npresione "0" para salir''') #se imprime lo que debe de hacer el usuario
                                                                  salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                  if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:# si presiona otro numero se hara lo siguiente
                                                                        print("presione 0") #se imprime la siguente instruccion
                                                                        continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                            pregunta_inventario = int(input("Cuanta memoria ram va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                            if pregunta_inventario > int(inventario[1][2]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                  1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                            elif pregunta_inventario <= int(inventario[1][2]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                  inventario[1][2] = int(inventario[1][2]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                            if preguntados ==1 :# si el usuario selecciona 1 se hara lo siguiente
                                                                  lista_productos.append(productosCorsair[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                  lista_productos.append(productosCorsair[2])#se agrega a la lista el precio
                                                                  lista_productos.append(productosCorsair[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                  precio.append(productosCorsair[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosCorsair[0] ,"$",productosCorsair[2],"c/u","Total:",productosCorsair[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                  lista_productos.append(productosCorsair[3])#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                  lista_productos.append(productosCorsair[5])#se agrega a la lista el precio
                                                                  lista_productos.append(productosCorsair[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                  precio.append(productosCorsair[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosCorsair[3] ,"$",productosCorsair[5],"c/u","Total:",productosCorsair[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                  lista_productos.append(productosCorsair[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                  lista_productos.append(productosCorsair[8])#se agrega a la lista el precio
                                                                  lista_productos.append(productosCorsair[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                  precio.append(productosCorsair[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosCorsair[6] ,"$",productosCorsair[8],"c/u","Total:",productosCorsair[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                  print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                      except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                            print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------") #se imprime lo siguiente  
                                                      except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                                  print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")    #se imprime lo siguiente
                                          break #ponemos un break para romper el ciclo.
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                  elif pregunta== 2 :#Si el ususario escribio bien la segunda marca se hara lo siguiente 
                         while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    lista_productos = ["RAM"]#Se asigna el tipo de producto en la lista
                                    Kingston  = "Kingston "#Hacemos una variable donde la marca sea igual a la palabra de la marca
                                    lista_productos.append(Kingston )##Agregamos la marca a la lista de productos que creamos
                                    print("\nLos productos son:\n 1.) Kingston 8 Ram - $600 \n 2.) Kingston 16 Ram- $1500 \n 3.) Kingston 32 Ram - $3000 \n")#Imprimimos la lista de productos con el presio
                                    productosKingston  = ["Kingston 8 Ram" , "$",  600 , "Kingston 16 Ram" , "$", 1500 , "Kingston 32 Ram", "$", 3000]#Asiganmos una lista de productos donde se guardara en una lista
                                          #                    0            1     2           3           4    5        6          7    8
                                    try:  #ponemos un try para que nos marque e impirma el error
                                          while True: #para seguir con el ciclo try
                                                preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                                if preguntados >= 4 or preguntados <= 0: #excluir valores mayores y menores
                                                      print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                                else: #para seguir con el ciclo
                                                      while contador == 0: #mantener el try en ciclo
                                                            try:  #ponemos un try para que nos marque e impirma el error
                                                                  print("El inventario actual de",inventario[0][2],"\nson:",inventario[1][2])#imprimimos el invenario con el nombre y cantidad
                                                                  if int(inventario[1][2]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                        print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                        salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                        if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                        else:# si presiona otro numero se hara lo siguiente
                                                                              print("presione 0") #se imprime la siguente instruccion
                                                                              continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                                  pregunta_inventario = int(input("Cuanta memeoria ram va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                                  if pregunta_inventario > int(inventario[1][2]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                        1/0 # se crea una division para que de el error zero division en el try 
                                                                  elif pregunta_inventario <= int(inventario[1][2]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                        inventario[1][2] = int(inventario[1][2]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                                  if preguntados ==1 :## si el usuario selecciona 1 se hara lo siguiente
                                                                                    lista_productos.append(productosKingston[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                                    lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                                    lista_productos.append(productosKingston[2])#se agrega a la lista el precio
                                                                                    lista_productos.append(productosKingston[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                                    precio.append(productosKingston[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                                    lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                                    print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosKingston[0] ,"$",productosKingston[2],"c/u","Total:",productosKingston[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                                    contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                                    break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                                    lista_productos.append(productosKingston[3])#)#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                                    lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                                    lista_productos.append(productosKingston[5])#Se agregara a la lista el indice 5 que es el precio
                                                                                    lista_productos.append(productosKingston[5]*pregunta_inventario) #se agrega a la lista el precio
                                                                                    precio.append(productosKingston[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                                    lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                                    print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosKingston[3] ,"$",productosKingston[5],"c/u","Total:",productosKingston[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                                    contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                                    break #ponemos un break para romper el ciclo.     #ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true                                           
                                                                  elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                                    lista_productos.append(productosKingston[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                                    lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                                    lista_productos.append(productosKingston[8])#se agrega a la lista el precio
                                                                                    lista_productos.append(productosKingston[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                                    precio.append(productosKingston[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                                    lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                                    print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosKingston[6] ,"$",productosKingston[8],"c/u","Total:",productosKingston[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                                    contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                                    break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                                    print("\n--------------------------------------------------------------------------------------------Invalido\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                            except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                                              print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")   #se imprime lo siguiente
                                                            except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                                              print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                break #ponemos un break para romper el ciclo.                                    
                                    except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                          print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")
                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                        print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
            except ValueError: #ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente

def menu_almacenamiento():# Definimos la funcion para las opciones de de ordenar lista
      contador = 0#se crea un contador desde 0
      while contador == 0:#se crea un ciclo solo si el contador es igual a 0
            try:  #ponemos un try para que nos marque e impirma el error
                  lista_productos = ["Almacenamiento"]#Se asigna el tipo de producto en la lista
                  pregunta = int(input("\n1)Samsung\n2)Seagate\nPresione el numero de la marca que desee: "))#hacemos la pregunta sobre la primera categoria que son las marcas
                  if pregunta == 1:#Si el ususario escribio bien la primera marca se hara lo siguiente 
                        Samsung = "Samsung"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                        lista_productos.append(Samsung)#Agregamos la marca a la lista de productos que creamos
                        productosSamsung = ["Samsung SSD 250 GB" , "$",  800 , "Samsung SSD 500 GB" , "$", 1200 , "Samsung SSD 1 TB", "$", 1800]#Asiganmos una lista de productos donde se guardara en una lista
                              #                    0            1     2           3           4    5        6          7    8
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    while True: #para manteenr el try en ciclo
                                          print("\nLos productos son:\n 1.) Samsung SSD 250 GB - $800 \n 2.) Samsung SSD 500 GB - $1200 \n 3.) Samsung SSD 1 TB - $1800 \n")#Imprimimos la lista de productos con el presio
                                          preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                          if preguntados >= 4 or preguntados <= 0: #para excluir valores mayores y menores
                                                print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                          else: #seguir con el ciclo
                                                while contador == 0: #mantener el try con el ciclo
                                                      try:  #ponemos un try para que nos marque e impirma el error
                                                            print("El inventario actual de",inventario[0][3],"\nson:",inventario[1][3])#imprimimos el invenario con el nombre y cantidad
                                                            if int(inventario[1][3]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                  print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                  salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                  if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:# si presiona otro numero se hara lo siguiente
                                                                        print("presione 0") #se imprime la siguente instruccion
                                                                        continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                            pregunta_inventario = int(input("Cuantas memorias de almacenamiento va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                            if pregunta_inventario > int(inventario[1][3]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                  1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                            elif pregunta_inventario <= int(inventario[1][3]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                  inventario[1][3] = int(inventario[1][3]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista 
                                                            if preguntados ==1 :# si el usuario selecciona 1 se hara lo siguiente
                                                                  lista_productos.append(productosSamsung[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                  lista_productos.append(productosSamsung[2])#se agrega a la lista el precio
                                                                  lista_productos.append(productosSamsung[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                  precio.append(productosSamsung[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosSamsung[0] ,"$",productosSamsung[2],"c/u","Total:",productosSamsung[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                  lista_productos.append(productosSamsung[3])#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                  lista_productos.append(productosSamsung[5])#se agrega a la lista el precio
                                                                  lista_productos.append(productosSamsung[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                  precio.append(productosSamsung[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosSamsung[3] ,"$",productosSamsung[5],"c/u","Total:",productosSamsung[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                  lista_productos.append(productosSamsung[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                  lista_productos.append(productosSamsung[8])#Se agregara a la lista el indice 8 que es el precio
                                                                  lista_productos.append(productosSamsung[8]*pregunta_inventario) #se agrega a la lista el precio
                                                                  precio.append(productosSamsung[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosSamsung[6] ,"$",productosSamsung[8],"c/u","Total:",productosSamsung[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                  print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                      except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                            print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")   #se imprime lo siguiente
                                                      except ZeroDivisionError: #ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                            print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")    #se imprime lo siguiente
                                          break #ponemos un break para romper el ciclo.
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                              
                  elif pregunta == 2 :#Si el ususario escribio bien la segunda marca se hara lo siguiente 
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    lista_productos = ["Almacenamiento"]#Se asigna el tipo de producto en la lista
                                    Seagate = "Seagate"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                                    lista_productos.append(Seagate)##Agregamos la marca a la lista de productos que creamos
                                    print("\nLos productos son:\n 1.) Seagate SSD 250 GB - $900 \n 2.) Seagate SSD 500 GB - $1600 \n 3.) Seagate SSD 1 TB - $1800 \n")#Imprimimos la lista de productos con el presio
                                    productosSeagate = ["Seagate SSD 250 GB" , "$",  900 , "Seagate SSD 500 GB" , "$", 1600 , "Seagate SSD 1 TB", "$", 1800]#Asiganmos una lista de productos donde se guardara en una lista
                                          #                    0            1     2           3           4    5        6          7    8
                                    try:  #ponemos un try para que nos marque e impirma el error
                                          while True: #mantener el ciclo 
                                                preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                                if preguntados >= 4 or preguntados <= 0:
                                                      print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                                else: #mantener el ciclo
                                                      while contador == 0:
                                                            try:  #ponemos un try para que nos marque e impirma el error
                                                                  print("El inventario actual de",inventario[0][3],"\nson:",inventario[1][3])#imprimimos el invenario con el nombre y cantidad
                                                                  if int(inventario[1][3]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                        print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                        salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                        if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                        else:# si presiona otro numero se hara lo siguiente
                                                                              print("presione 0") #se imprime la siguente instruccion
                                                                              continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                                  pregunta_inventario = int(input("Cuantas memorias de almacenamiento va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                                  if pregunta_inventario > int(inventario[1][3]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                        1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                                  elif pregunta_inventario <= int(inventario[1][3]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                        inventario[1][3] = int(inventario[1][3]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                                        if preguntados ==1 :## si el usuario selecciona 1 se hara lo siguiente
                                                                                    lista_productos.append(productosSeagate[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                                    lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                                    lista_productos.append(productosSeagate[2]) #se agrega a la lista el precio
                                                                                    lista_productos.append(productosSeagate[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                                    precio.append(productosSeagate[2]*[pregunta_inventario])#Se agregara a la lista de precio el precio del producto
                                                                                    lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                                    print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosSeagate[0] ,"$",productosSeagate[2],"c/u","Total:",productosSeagate[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                                    contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                                    break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                        elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                                    lista_productos.append(productosSeagate[3])#)#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                                    lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                                    lista_productos.append(productosSeagate[5])#se agrega a la lista el precio
                                                                                    lista_productos.append(productosSeagate[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                                    precio.append(productosSeagate[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                                    lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                                    print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosSeagate[3] ,"$",productosSeagate[5],"c/u","Total:",productosSeagate[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                                    contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                                    break #ponemos un break para romper el ciclo. #ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true                                               
                                                                        elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                                    lista_productos.append(productosSeagate[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                                    lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                                    lista_productos.append(productosSeagate[8])#se agrega a la lista el precio
                                                                                    lista_productos.append(productosSeagate[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                                    precio.append(productosSeagate[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                                    lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                                    print("\n--------------------------------------------------------------------------------------------\n\nUsted eligio", pregunta_inventario,"CPU de",productosSeagate[6] ,"$",productosSeagate[8],"c/u","Total:",productosSeagate[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                                    contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                                    break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                        else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                                    print("\n--------------------------------------------------------------------------------------------Invalido\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                            except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")   #se imprime lo siguiente
                                                            except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                                  print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                break #ponemos un break para romper el ciclo.
                                    except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                          print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")
                              except ValueError: #ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                        print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
            except ValueError: #ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente

def menu_gpu():# Definimos la funcion para las opciones de de ordenar lista
      contador = 0#se crea un contador desde 0
      while contador == 0:#se crea un ciclo solo si el contador es igual a 0
            try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                  lista_productos = ["GPU"]#Se asigna el tipo de producto en la lista
                  pregunta = int(input("\n1)Nvidia\n2)AMD\nPresione el numero de la marca que desee: "))#hacemos la pregunta sobre la primera categoria que son las marcas
                  if pregunta == 1 :#Si el ususario escribio bien la primera marca se hara lo siguiente 
                        Nvidia = "Nvidia"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                        lista_productos.append(Nvidia)#Agregamos la marca a la lista de productos que creamos
                        productosNvidia = ["Nvidia Geforce 4060" , "$",  10000 , "Nvidia Geforce 4070" , "$", 15000 , "Nvidia Geforce 4080", "$", 25000]#Asiganmos una lista de productos donde se guardara en una lista
                              #                    0            1     2           3           4    5        6          7    8
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    while True: # para mantener el ciclo
                                          print("\nLos productos son:\n 1.) Nvidia Geforce 4060 - $10000 \n 2.) Nvidia Geforce 4070 - $15000 \n 3.) Nvidia Geforce 4080 - $25000 \n")#Imprimimos la lista de productos con el presio
                                          preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                          if preguntados >= 4 or preguntados <= 0: #para excluir valores mayores y menores
                                                print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                          else: #seguir con el ciclo
                                                 while contador == 0: #seguir con el ciclo
                                                      try:  #ponemos un try para que nos marque e impirma el error
                                                            print("El inventario actual de",inventario[0][4],"\nson:",inventario[1][4])#imprimimos el invenario con el nombre y cantidad
                                                            if int(inventario[1][4]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                  print('''No tenemos inventario de aquel producto\nPresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                  salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                  if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:# si presiona otro numero se hara lo siguiente
                                                                        print("presione 0") #se imprime la siguente instruccion
                                                                        continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                            pregunta_inventario = int(input("Cuantos GPU va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                            if pregunta_inventario > int(inventario[1][4]) or pregunta_inventario < 0:  #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                  1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                            elif pregunta_inventario <= int(inventario[1][4]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                  inventario[1][4] = int(inventario[1][4]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista 
                                                            if preguntados ==1 :# si el usuario selecciona 1 se hara lo siguiente
                                                                  lista_productos.append(productosNvidia[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                  lista_productos.append(productosNvidia[2]) #se agrega a la lista el precio
                                                                  lista_productos.append(productosNvidia[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                  precio.append(productosNvidia[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosNvidia[0] ,"$",productosNvidia[2],"c/u","Total:",productosNvidia[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                  lista_productos.append(productosNvidia[3])#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                  lista_productos.append(productosNvidia[5])#se agrega a la lista el precio
                                                                  lista_productos.append(productosNvidia[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                  precio.append(productosNvidia[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosNvidia[3] ,"$",productosNvidia[5],"c/u","Total:",productosNvidia[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                  lista_productos.append(productosNvidia[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                  lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidada
                                                                  lista_productos.append(productosNvidia[8])#se agrega a la lista el precio
                                                                  lista_productos.append(productosNvidia[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                  precio.append(productosNvidia[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                  lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                  print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosNvidia[6] ,"$",productosNvidia[8],"c/u","Total:",productosNvidia[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                  contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                  break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                            else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                  print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                      except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                                            print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")   #se imprime lo siguiente
                                                      except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                            print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")  #se imprime lo siguiente
                                          break #ponemos un break para romper el ciclo.
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                  elif pregunta == 2:#Si el ususario escribio bien la segunda marca se hara lo siguiente 
                        while contador == 0: #se crea un ciclo solo si el contador es igual a 0
                              try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                                    lista_productos = ["GPU"]#Se asigna el tipo de producto en la lista
                                    AMD = "AMD"#Hacemos una variable donde la marca sea igual a la palabra de la marca
                                    lista_productos.append(AMD)##Agregamos la marca a la lista de productos que creamos
                                    print("\nLos productos son:\n 1.) AMD RX 7900 XTX - $20000 \n 2.) AMD RX 6500 XT - $14000 \n 3.) AMD RX 6000 XT - $10000 \n")#Imprimimos la lista de productos con el presio
                                    productosAMD = ["AMD RX 7900 XTX" , "$",  20000 , "AMD RX 6500 XT" , "$", 14000 , "AMD RX 6000 XT", "$", 10000]#Asiganmos una lista de productos donde se guardara en una lista
                                          #                    0            1     2           3           4    5        6          7    8
                                    try:  #ponemos un try para que nos marque e impirma el error
                                          while True: #se crea un ciclo para el try
                                                preguntados = int(input("Ingrese el número del producto: "))#preguntamos el numero del producto que desee el usuario
                                                if preguntados >= 4 or preguntados <= 0:#excluye cantidades mayores y menores
                                                      print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                                else: #se mantiene el try
                                                      while contador == 0: #se mantienen el try
                                                            try:  #ponemos un try para que nos marque e impirma el error
                                                                  print("El inventario actual de",inventario[0][4],"\nson:",inventario[1][4])#imprimimos el invenario con el nombre y cantidad
                                                                  if int(inventario[1][4]) == 0: # si la cantidad es igual a 0 se hara lo sigiente
                                                                        print('''No tenemos inventario de aquel producto\npresione "0" para salir''')#se imprime lo que debe de hacer el usuario
                                                                        salir = int(input(" "))# ponemos un imput para que el usuario pueda escribir
                                                                        if salir == 0:#si el usuario presiona 0 se hara lo siguiente
                                                                              contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                              break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                        else:# si presiona otro numero se hara lo siguiente
                                                                              print("presione 0") #se imprime la siguente instruccion
                                                                              continue # se pone continue para que vuelva a repetir el proceso desde el if
                                                                  pregunta_inventario = int(input("Cuantos GPU va a querer?")) #se pregunta la cantidad de producto que va a querer el usuario
                                                                  if pregunta_inventario > int(inventario[1][4]) or pregunta_inventario < 0: #si recribe un numero mayor de los que hay, se hara lo sigiente
                                                                        1/0#Se crea una division de un numero entre 0 para que marque un error y evite el proceso
                                                                  elif pregunta_inventario <= int(inventario[1][4]): #si escribe un numeor menor o igual de la cantidad del inventario, se hara lo siguiente
                                                                        inventario[1][4] = int(inventario[1][4]) - pregunta_inventario#se hace la resta de la cantidad menos la seelccion y se guarda en la lista
                                                                  if preguntados ==1 :## si el usuario selecciona 1 se hara lo siguiente
                                                                        lista_productos.append(productosAMD[0])#Se agregara a la lista el indice 0 que es el nombre del producto
                                                                        lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                        lista_productos.append(productosAMD[2])#se agrega a la lista el precio
                                                                        lista_productos.append(productosAMD[2]*pregunta_inventario)#Se agregara a la lista el indice 2 que es el precio
                                                                        precio.append(productosAMD[2]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                        lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                        print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[0] ,"$",productosAMD[2],"c/u","Total:",productosAMD[2]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  elif preguntados ==2 :# si el usuario selecciona 2 se hara lo siguiente
                                                                        lista_productos.append(productosAMD[3])#)#Se agregara a la lista el indice 3 que es el nombre del producto
                                                                        lista_productos.append(pregunta_inventario) #se agrega a la lista la cantidad
                                                                        lista_productos.append(productosAMD[5])#se agrega a la lista el precio
                                                                        lista_productos.append(productosAMD[5]*pregunta_inventario)#Se agregara a la lista el indice 5 que es el precio
                                                                        precio.append(productosAMD[5]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                        lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                        print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[3] ,"$",productosAMD[5],"c/u","Total:",productosAMD[5]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  elif preguntados ==3 :# si el usuario selecciona 2 se hara lo siguiente
                                                                        lista_productos.append(productosAMD[6])#Se agregara a la lista el indice 6 que es el nombre del producto
                                                                        lista_productos.append(pregunta_inventario)#se agrega a la lista la cantidad
                                                                        lista_productos.append(productosAMD[8])#se agrega a la lista el precio
                                                                        lista_productos.append(productosAMD[8]*pregunta_inventario)#Se agregara a la lista el indice 8 que es el precio
                                                                        precio.append(productosAMD[8]*pregunta_inventario)#Se agregara a la lista de precio el precio del producto
                                                                        lista.append(lista_productos)# Se agrega la lista la lista de productos
                                                                        print("\n--------------------------------------------------------------------------------------------\nUsted eligio", pregunta_inventario,"CPU de",productosAMD[6] ,"$",productosAMD[8],"c/u","Total:",productosAMD[8]*pregunta_inventario ,"Pesos\n--------------------------------------------------------------------------------------------")# Se imprime el producto y el precio que eligio el usuario
                                                                        contador += 1#le sumamos al contador 1 para que ya no se a igual a 0 y se rompa el ciclo
                                                                        break #ponemos un break para romper el ciclo.#ponemos un break #ponemos un break para romper el ciclo. para romper el ciclo while true
                                                                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                                                                        print("\n--------------------------------------------------------------------------------------------Invalido\n--------------------------------------------------------------------------------------------")#Se imprime invalido
                                                            except ValueError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")   #se imprime lo siguiente
                                                            except ZeroDivisionError:#ponemos un except de division entre 0 para que marque el error de la cantidad de inventario
                                                                  print("\n--------------------------------------------------------------------------------------------\nNo tenemos esa cantidad en el inventario, seleccione otra cantidad\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                                break #ponemos un break para romper el ciclo.
                                    except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                          print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                              except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                                    print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                  else:#Si el usuario pone algo erroneo se hara lo siguiente
                        print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")#Se imprime invalido
            except ValueError: 
                  print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente

def suma(): #definimos suma
  suma = sum(precio)#se suna todad la lista de precio acumulados con la funcion suma
  print("-------------------------------------------------------\nEl Monto total es de: $", suma,"Pesos")#se imprime la suma de todos los productos

empleado = input("Introduzca su nombre: ")  # Solicita el nombre del empleado y lo almacena en la variable 'empleado'

while True:  # Inicia un bucle infinito para que el programa se ejecute continuamente hasta que se elija la opción de salir
    print("--------------------------------------------------------------------------------------------")  # Imprime una línea separadora para mejorar la legibilidad
    print("Hola", empleado, "¿Cómo le va el dia de hoy?")  # Saluda al empleado por su nombre
    print("Sea bienvenido a Building Bit Center")  # Muestra un mensaje de bienvenida
    print("--------------------------------------------------------------------------------------------")  # Imprime otra línea separadora
    print("MENU")  # Muestra el título del menú
    print("1) Ordenar productos")  # Opción para ordenar productos
    print("2) Agregar inventario de alguno de los productos")  # Opción para agregar productos al inventario
    print("3) Imprimir inventario actual de los productos")  # Opción para mostrar el inventario actual
    print("4) Monto total de ventas")  # Opción duplicada (posible error)
    print("5) Salir del programa")  # Opción para salir del programa
    print("--------------------------------------------------------------------------------------------")  # Imprime otra línea separadora

    # Estructura condicional para evaluar la opción seleccionada
    
    try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error  
      opcion = int(input("Elige la opcion que desee "))  # Solicita al usuario que ingrese una opción y la convierte a un número entero
      if opcion == 1: # Cuando el usuario ponga 1 seguira con la condicion del numero 1
            lista.clear() #Se borra la lista cada vez que se elige la opcion 1
            lista_productos.clear() #Se borra la lista de los productos cada vez que elige la opcion 1
            while True: # Se crea un ciclo infinito
                  x = 0 # se asigna un contador x
                  for i in range(5): #se crea un ciclo for de i en el rango de 5 
                        x += 1 #se suma x por cada rango para que el usuario sepa que numero elegir ")"
                        print(x ,")", inventario[0][i]) # se imprime los productos
                  print("6 ) Imprimir Nota") #Se imprime la nota de los productos
                  print("7 ) Regresar al menu principal") #Se imprime la opcion de regresar al menu principal
                  try:  #ponemos un try para que nos marque e impirma el error#ponemos un try para que nos marque e impirma el error
                        opcion = int(input("Ingrese su opción: ")) #El ususario ingresa que opcion del menu quiere
                        if opcion == 1: #si el usuario eligio opcion 1 se hara lo siguiente
                              menu_cpu() #Si la opcion es 1 se ira a la def de menu_cpu
                        elif opcion == 2: #si el usuario eligio opcion 2 se hara lo siguiente
                              menu_motherboard()  #Si la opcion es 2 se ira a la def de menu_motherboard
                        elif opcion == 3: #si el usuario eligio opcion 3 se hara lo siguiente
                              menu_ram()  #Si la opcion es 3 se ira a la def de menu_ram
                        elif opcion == 4: #si el usuario eligio opcion 4 se hara lo siguiente
                              menu_almacenamiento()  #Si la opcion es 4 se ira a la def de menu_almacenamiento
                        elif opcion == 5: #si el usuario eligio opcion 5 se hara lo siguiente
                              menu_gpu()  #Si la opcion es 5 se ira a la def de menu_gpu
                        elif opcion == 6: #si el usuario eligio opcion 6 se hara lo siguiente
                              monto_total = 0 # se asigna el monto en 0
                              print("Sus porductos son loa siguientes\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                              #Se imprime el titulo y el separador
                              for i in lista:#se crea uba lista i por cada elemnto en la lista
                                    print("Tipo de producto ({:1}) Marca: ({:1}) Producto: ({:1}) Cantidad: ({:1}) Precio: ({:1}$ pesos) Total: {:1}$ pesos)".format(*i),"\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                                    #se imprime  el boleto asiganndo los indices de cada lista
                              for x in lista: # se crea un ciclo for de x en cada elemento de la lista
                                    for j in x: # se crea otro ciclo for en j en cada elemnto de x
                                          if isinstance(j, (int)):  # Verifica si el elemento es numérico
                                                monto_total += j #se hace la opreacion del monto donde se sumara cada elemento numerico de la lista
                              print("La suma total es: $", monto_total,"pesos\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
                        elif opcion == 7: #si el usuario eligio opcion 7 se hara lo siguiente
                              break #ponemos un break para romper el ciclo. #Si la usuario eligio opcion 7 se sale del ciclo del menu de ordenar productos
                        else: #Si el usuario escribe un caracter que no es mencionado se hara lo siguiente
                              print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------") #Imprime que es invalido
                  except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
                        print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente

      elif opcion == 2: # Cuando el usuario ponga 2 seguira con la condicion del numero 2
            contador_inventario = 0 # se crea un contador que inicie en 0
            while contador_inventario == 0: # se crea un while qdel contador que sea 0
                  try:  #ponemos un try para que nos marque e impirma el error
                        x = 0 # se crea un contador x
                        for i in range(5): #se crea un ciclo for de i en el rango de 5 
                                    x += 1 #se suma x por cada rango para que el usuario sepa que numero elegir ")"
                                    print(x ,")", inventario[0][i],inventario[1][i]) # se imprime los productos
                        mas_invenatrio = int(input("Tecle el numero del producto que quiere agregar: ")) #ingresa el numero del producto que quiere agregar
                        while True: #se crea un ciclo
                              try:  #ponemos un try para que nos marque e impirma el error
                                    if mas_invenatrio == 1:#cuandoe el usuario elija 1
                                          agrega = int(input("Ingrese la cantidad de inventario que va agregar: ")) #ingresa la cantidad a agregar
                                          if agrega < 0: #se excluye cantidades menores a 0
                                                 print("No se puede poner numeros negativos, ingrese otra cantidad") #imprime la causa del error
                                                 break #se quiebrea el ciclo para que el usuario ingrese una nueva opcion
                                          else: # si es mayor que sero se hace lo siguiente
                                                inventario[1][0] = int(inventario[1][0]) + agrega #se calcula la suma
                                                print("Unsted agrego, ",agrega, "productos en ", inventario[0][0]) #imprime el mensaje de la suma 
                                                contador_inventario += 1 #se le suma el contador para romper el ciclo
                                                break #ponemos un break para romper el ciclo.
                                    elif mas_invenatrio == 2:#cuandoe el usuario elija 2
                                          agrega = int(input("Ingrese la cantidad de inventario que va agregar: ")) #ingresa la cantidad a agregar
                                          if agrega < 0: #se excluye cantidades menores a 0
                                                 print("No se puede poner numeros negativos, ingrese otra cantidad") #imprime la causa del error
                                                 break #se quiebrea el ciclo para que el usuario ingrese una nueva opcion
                                          else: # si es mayor que sero se hace lo siguiente
                                                inventario[1][1] = int(inventario[1][1]) + agrega#se calcula la suma
                                                print("Unsted agrego, ",agrega, "productos en ", inventario[0][1])#imprime el mensaje de la suma
                                                contador_inventario += 1#se le suma el contador para romper el ciclo
                                                break #ponemos un break para romper el ciclo.
                                    elif mas_invenatrio == 3:#cuandoe el usuario elija 3
                                          agrega = int(input("Ingrese la cantidad de inventario que va agregar: ")) #ingresa la cantidad a agregar
                                          if agrega < 0: #se excluye cantidades menores a 0
                                                 print("No se puede poner numeros negativos, ingrese otra cantidad") #imprime la causa del error
                                                 break #se quiebrea el ciclo para que el usuario ingrese una nueva opcion
                                          else: # si es mayor que sero se hace lo siguiente
                                                inventario[1][2] = int(inventario[1][2]) + agrega#se calcula la suma
                                                print("Unsted agrego, ",agrega, "productos en ", inventario[0][2])#imprime el mensaje de la suma
                                                contador_inventario += 1#se le suma el contador para romper el ciclo
                                                break #ponemos un break para romper el ciclo.
                                    elif mas_invenatrio == 4:#cuandoe el usuario elija 4
                                          agrega = int(input("Ingrese la cantidad de inventario que va agregar: ")) #ingresa la cantidad a agregar
                                          if agrega < 0: #se excluye cantidades menores a 0
                                                 print("No se puede poner numeros negativos, ingrese otra cantidad") #imprime la causa del error
                                                 break #se quiebrea el ciclo para que el usuario ingrese una nueva opcion
                                          else: # si es mayor que sero se hace lo siguiente
                                                inventario[1][3] = int(inventario[1][3]) + agrega#se calcula la suma
                                                print("Unsted agrego, ",agrega, "productos en ", inventario[0][3])#imprime el mensaje de la suma
                                                contador_inventario += 1#se le suma el contador para romper el ciclo
                                                break #ponemos un break para romper el ciclo.
                                    elif mas_invenatrio == 5:#cuandoe el usuario elija 5
                                          agrega = int(input("Ingrese la cantidad de inventario que va agregar: ")) #ingresa la cantidad a agregar
                                          if agrega < 0: #se excluye cantidades menores a 0
                                                 print("No se puede poner numeros negativos, ingrese otra cantidad") #imprime la causa del error
                                                 break #se quiebrea el ciclo para que el usuario ingrese una nueva opcion
                                          else: # si es mayor que sero se hace lo siguiente
                                                inventario[1][4] = int(inventario[1][4]) + agrega#se calcula la suma
                                                print("Unsted agrego, ",agrega, "productos en ", inventario[0][4])#imprime el mensaje de la suma
                                                contador_inventario += 1#se le suma el contador para romper el ciclo
                                                break #ponemos un break para romper el ciclo.
                                    else: #para valores invalidos
                                          print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")
                                          break #ponemos un break para romper el ciclo.
                              except ValueError: #se crea para detectar un error de valor
                                     print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")
                  except ValueError: #se crea para detectar un error de valor
                         print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")

      elif opcion == 3: #Como el usuario eligio 3 se imprime la opcion 3 que es Ordenar porductos
            print("--------------------------------------------------------------------------------------------\nInventario actual de objetos\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente
            for i in range(5): #se crea un ciclo for de i en el rango de 5 
                        print(inventario[0][i],inventario[1][i]) # se imprime los productos #se imprime el inventario del archivo csv en lista
      elif opcion == 4: # Cuando el usuario ponga 4 seguira con la condicion del numero 4
            suma()  # cuando el usuario ponaga 4 se ejecutara la def de suma que dara el monto 
      elif opcion == 5: # Cuando el usuario ponga 5 seguira con la condicion del numero 5 
            print("Adios", empleado, "gracias por usar el programa") #Se imprime salir 
            break #ponemos un break para romper el ciclo.  # Sale del bucle cuando se elige la opción 5
      else: # Aqui va todos los valores que no estan en la condicional 
            print("\n--------------------------------------------------------------------------------------------\nEl número ingresado no es correcto\n--------------------------------------------------------------------------------------------")  # Muestra un mensaje de error si la opción no es válida
    except ValueError:#ponemos un except para que detecte si hay un problema de valor e imprima lo siguiente y nos de chace en teclear algo mas
      print("\n--------------------------------------------------------------------------------------------\nParece que hubo un error en los caracteres ingresados, ingrese nuevamente el numero\n--------------------------------------------------------------------------------------------")#se imprime lo siguiente

with open('invetnario.csv', 'w', newline='') as csvfile: #abrimos el archivo como w para editarlo
      actalizacion = csv.writer(csvfile) #hacemos una variable para sobrescribir el archivo
      actalizacion.writerows(inventario) #con el writerows ponemos nuestra lista para que se sobrescriba 
csvfile.close() #Cerrarmos el archivo y se gaurda los cambios
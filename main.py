import random  # Importamos la librería random
import time #Importamos la libreria de tiempo
#Creamos las variables para los colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (BLUE+"Bienvenido a mi trivia sobre Dragon Ball Z"+RESET)
print ("Demuestra qué tan fanático eres de Dragón Ball Z, la popular obra de Akira Toriyama y responde la siguiente preguntas:")

#Preguntamos nombre del jugador y los almacenamos en una variable
nombre_saiyajin = input("Ingresa tu nombre Saiyajin: ")
#Mostramos mensaje de Bienvenida, indicandole las instrucciones.
print ("\n Hola Saiyajin",YELLOW + nombre_saiyajin + RESET, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta por cada respuesta correcta sumas puntos y por cada respuesta incorrecta se te restaran puntos:\n")

#Lista de preguntas
lista_preguntas=["\n1) ¿Quiénes estaban en Kame House cuando Gokú fue a presentar a su hijo Gohan?",
"\n2) ¿Qué técnicas le enseño Kaio-Sama a Goku?",
"\n3) ¿Cómo se llama el planeta natal de Piccolo?",
"\n4) ¿Qué hizo posible que Gokú se transforme en Super Saiyajin?",
"\n5) ¿Cuántos Cells Jr. creó Cell durante el torneo que él mismo organizó?",
"\n6) ¿De quiénes se despide Majin Vegeta antes de sacrificar su vida durante la pelea con Majin Buu?",
"\n7) ¿Cuál es la transformación más fuerte de Gokú en Dragon Ball Z?",
"\n8) ¿Cómo se llama el hermano menor de Gohan?",
"\n9) ¿Cuántos hijos tiene Vegeta?"]
#Lista de alternativas
lista_alternativas=[
  ["a) La tortuga marina, el maestro Roshi, Bulma y Krilin",
   "b) Yamcha, Krilin, Bulma",
   "c) El maestro Roshi, la tortuga marina y Krilin",
   "d) Bulma, el maestro Roshi y Krilin",
   "a"],
  ["a) Kame Hame Ha y Kaio-Ken",
   "b) Kaio-Ken y Genki-dama",
   "c) Kame Hame Ha y Makankosappo",
   "d) Genki-dama y Makankosappo",
   "b"],
  ["a) Planeta Supremo",
   "b) Planeta Vegeta",
   "c) Planeta Tierra",
   "d) Namekusei",
   "d"],
  ["a) La muerte de Gohan",
   "b) La muerte de Piccolo",
   "c) La muerte de Krilin",
   "d) La muerte de Vegeta",
   "c"],
  ["a) 5",
   "b) 6",
   "c) 8",
   "d) 7",
   "d"],
  ["a) Bulma, Trunks y Kakarotto",
   "b) Bulma y Trunks",
   "c) Bulma y Kakarotto",
   "d) Trunks y Kakarotto",
   "a"],
  ["a) Super Saiyajin 4",
   "b) Super Saiyajin 3",
   "c) Super Saiyajin 2",
   "d) Super Saiyajin",
   "b"],
  ["a) Trunks",
   "b) Tarble",
   "c) Goten",
   "d) Krilin",
   "c"],
  ["a) 3",
   "b) 4",
   "c) 5",
   "d) 2",
   "d"]
]
#Creamos lista para guardar los puntajes de los intentos
puntaje_total=[]
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    #creamos variable para puntaje
    puntaje = random.randint(0, 10)
    #Creamos lista para almacenar los puntajes obtenidos por preguntas.
    lista_puntajes=[]
    lista_puntajes.append(puntaje)
    #Mostramos una mensaje para decirle al jugador con cuantos puntos inicia
    if intentos > 1:
      print("\nBienvenido de nuevo Saiyajin: " +YELLOW+nombre_saiyajin+RESET)
      print(GREEN + f"Intento número {intentos}" + RESET)
    print("Inicias con",GREEN ,puntaje , RESET, "puntos.\n")
    print("Espere Cargando Preguntas")
    for numero_carga in range (1,6,+1):
        print("Cargando.....",numero_carga*20,"%")
        time.sleep(1)
    # Pregunta 1
    for n_p in range(0,len(lista_preguntas)):
      print (MAGENTA+lista_preguntas[n_p]+RESET)
      for n_a in range(0,len(lista_alternativas[n_p])-1):
          print(lista_alternativas[n_p][n_a])
          
    #Almacenamos la respuesta del usuario en la variable "respuesta_1"
      respuesta = input(BLUE+"\nTu respuesta: "+RESET)
      while respuesta not in ("a", "b", "c", "d"):
          respuesta = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    #Verificamos si ha seleccionado la respuesta correcta y le sumamos puntos
      if respuesta == lista_alternativas[n_p][4]:
        #puntaje += random.randint(5, 10)
        puntaje = random.randint(5, 10)
        lista_puntajes.append(puntaje)
        print ("Muy bien Saiyajin", YELLOW+nombre_saiyajin+RESET, "!")
        print ("Has ganado ", GREEN,puntaje,RESET, " puntos.")
      else:
        #puntaje -= random.randint(1, 4)
        puntaje = random.randint(-5, -1)
        lista_puntajes.append(puntaje)
        print (RED+"Respuesta Incorrecto!"+RESET)
        print ("Has perdido ", RED,puntaje,RESET, " puntos.")
    
      time.sleep(1)
         
    # Pregunta Bonus
    print (BLUE+"\nLa siguiente pregunta es un Bonus"+RESET)
    print (MAGENTA+"\n10) ¿Cuántas estrellas tenia la esfera que le regaló su abuelo a Gokú?"+RESET)
    
    num_estrellas = input(BLUE+"\nTu respuesta: "+RESET)
    while num_estrellas.isnumeric() == False:
        num_estrellas = input ("Debes ingresar un número. Ingresa nuevamente tu respuesta: ")
 
    if int(num_estrellas) == 4:
        print ("Muy bien Saiyajin", YELLOW+nombre_saiyajin+RESET, "!")
        print ("Tu puntaje se multiplica por ", GREEN,"*2",RESET, ".")
        print("Puntaje alcanzado: ", GREEN,sum(lista_puntajes),RESET ," puntos")
        nvo_puntaje = sum(lista_puntajes)*2
        print("Puntaje aplicando bonus: ", GREEN,nvo_puntaje,RESET ," puntos")
    elif int(num_estrellas) >= 7:
        print (RED+"Totalmente incorrecto"+RESET+" Saiyajin", YELLOW+nombre_saiyajin+RESET, "!")
        print ("Tu puntaje sera dividido por ", RED,"/2",RESET, ".")
        print("Puntaje alcanzado: ", GREEN,sum(lista_puntajes),RESET ," puntos")
        nvo_puntaje = sum(lista_puntajes)/2
        print("Puntaje aplicando bonus: ", GREEN,nvo_puntaje,RESET ," puntos")
    elif int(num_estrellas)==5 or int(num_estrellas)==6:
        print (RED+"Incorrecto"+RESET+" Saiyajin", YELLOW+nombre_saiyajin+RESET, "!")
        print ("Tu puntaje sera restado por ", RED,"-5",RESET, ".")
        print("Puntaje alcanzado: ", GREEN,sum(lista_puntajes),RESET ," puntos")
        nvo_puntaje = sum(lista_puntajes)-5
        print("Puntaje aplicando bonus: ", GREEN,nvo_puntaje,RESET ," puntos")
    else:
        print (YELLOW+"Casi"+RESET+" Saiyajin", YELLOW+nombre_saiyajin+RESET, "!")
        print ("Tu puntaje sera sumado por ", RED,"+5",RESET, ".")
        print("Puntaje alcanzado: ", GREEN,sum(lista_puntajes),RESET ," puntos")
        nvo_puntaje = sum(lista_puntajes)+5
        print("Puntaje aplicando bonus: ", GREEN,nvo_puntaje,RESET ," puntos")
    print("\nGracias Saiyajin ",YELLOW+nombre_saiyajin+RESET," por jugar mi trivia, alcanzaste ", GREEN,nvo_puntaje,RESET ," puntos")
    print(YELLOW+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
    repetir_trivia = input(BLUE+"Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
    reg_puntaje = "Total de puntos Intento "+str(intentos)+" : "+str(nvo_puntaje) 
    puntaje_total.append(nvo_puntaje)

    if repetir_trivia != "si":  #!= significa "distinto"
        print("\nEspero Saiyajin " +YELLOW+ nombre_saiyajin +RESET+ " que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False  #Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
        print("Tus puntajes obtenidos son:\n")  
        for i in range(0,len(puntaje_total)):
          print("Total de puntos Intento ", i+1," : ",puntaje_total[i])
        print(GREEN+"\nPuntaje Máximo obteniido: " +str(max(puntaje_total))+ "" +RESET)
        print(RED+"\nPuntaje Mínimo obteniido: " +str(min(puntaje_total)) + "" +RESET)
    









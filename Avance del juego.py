
a=("!Hola! Bienvenido a uno de los juegos más populares,")
b=('bienvenido a "piedra, papel o tijera".')
print(a,b)
b=1
c=2
jugar=int(input(f"""¿Listo para divertirte? (tienes 3 intentos)
-Presiona {b} si deseas jugar o {c} si deseas salir.
"""))
while jugar==2:
    print("Volverás a la pantalla de inicio...")  
    a=("!Hola! Bienvenido a uno de los juegos más populares,")
    b=('bienvenido a "piedra, papel o tijera".')
    print(a,b)
    b=1
    c=2
    jugar=int(input(f"""¿Listo para divertirte? (tienes 3 intentos)
-Presiona {b} si deseas jugar o {c} si deseas salir.
"""))

if jugar==1:
    print("Comienza el juego...")         

else:
      print("Ingresa una opción válida por favor.")

opcionusuario=int(input('''Selecciona tu "arma":
          
-Presiona 1 para escoger piedra.
-Presiona 2 para escoger papel.
-Presiona 3 para escoger tijera.
'''))
if (opcionusuario==1 or opcionusuario==2 or opcionusuario==3):
    print("Ahora es el turno de tu rival...")
else:
      int(input("Selecciona una opción válida:"))
import random
numerorival= random.randint(1,3)
if numerorival==1:
    print("Tu rival seleccionó: piedra.")
elif numerorival==2:
    print("Tu rival seleccionó: papel.")
else:
     print("Tu rival seleccionó: tijera.")
for intentos in range(0,3):
     if intentos>=3: 
        break
if opcionusuario==numerorival:
     print("""
    ¡Casi, es un emapte!""")
if opcionusuario==1 and numerorival==2 or opcionusuario==2 and numerorival==3 or opcionusuario==3 and numerorival==1:
     print("""
    Lo siento, has perdido.""")
elif opcionusuario==1 and numerorival==3 or opcionusuario==2 and numerorival==1 or opcionusuario==3 and numerorival==2:
    print("""
    ¡Felicidades, has ganadoooo!""")
print(f"""
Tienes {intentos} intentos más.""")
for intentos in range (1,-1,-1):
     if intentos==0:
          print(f"""
No te quedan mas intentos.""")
     print(f"""
Tienes {intentos} intentos más.""")
     
     
     
     
     

     
     
          
          
     

     
     






    




          



    





























    

     








































e=("Creado por: Nicolás García")
print(e)
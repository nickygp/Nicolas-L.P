#defino mi función y su parámetro
def intento_restante(intentos=3):
     if intentos<=1:
        print("No te quedan más intentos.")
     else:
        print(f"Te quedan {intentos-1} intentos.")

#bienvenida al juego
a=("!Hola! Bienvenido a uno de los juegos más populares,")
b=('bienvenido a "piedra, papel o tijera".')
print(a,b)
b=1
c=2
jugar=int(input(f"""¿Listo para divertirte? (tienes 3 intentos)
-Presiona {b} si deseas jugar o {c} si deseas salir.
"""))

#while sobre que si no deseas jugar vuelves a pantalla de inicio
while jugar==2:
    print("Volverás a la pantalla de inicio...")  
    a=("!Hola! Bienvenido a uno de los juegos más populares,")
    b=('bienvenido a "piedra, papel o tijera".')
    print(a,b)
    b=1
    c=2
    jugar=int(input(f"""¿Listo para divertirte? (tienes 3 intentos)2
-Presiona {b} si deseas jugar o {c} si deseas salir.
"""))

if jugar==1:
    print("Comienza el juego...")         

else:
      print("Ingresa una opción válida por favor.")

#selección del usuario para jugar
opcionusuario=int(input('''-Selecciona tu "arma":
          
-Presiona 1 para escoger piedra.
-Presiona 2 para escoger papel.
-Presiona 3 para escoger tijera.
'''))
if opcionusuario>3:
     print("Selecciona una opción válida por favor:")
elif (opcionusuario==1 or opcionusuario==2 or opcionusuario==3):
    print("Ahora es el turno de tu rival...")

#número aleatorio para el turno de la pc
import random
numerorival= random.randint(1,3)
if numerorival==1:
    print("Tu rival seleccionó: piedra.")
elif numerorival==2:
    print("Tu rival seleccionó: papel.")
else:
     print("Tu rival seleccionó: tijera.")

#avisos sobre si ganaste, perdiste o empataste
if opcionusuario==numerorival:
     print("""
¡Casi, es un emapte!""")
if opcionusuario==1 and numerorival==2 or opcionusuario==2 and numerorival==3 or opcionusuario==3 and numerorival==1:
     print("""
Lo siento, has perdido.""")
elif opcionusuario==1 and numerorival==3 or opcionusuario==2 and numerorival==1 or opcionusuario==3 and numerorival==2:
    print("""
¡Felicidades, has ganadoooo!""")
#invocamos a la función para el primer intento
intento_restante()
opcionusuario=int(input('''-Selecciona tu "arma":
          
-Presiona 1 para escoger piedra.
-Presiona 2 para escoger papel.
-Presiona 3 para escoger tijera.
'''))
if opcionusuario>3:
     print("Selecciona una opción válida por favor:")
elif (opcionusuario==1 or opcionusuario==2 or opcionusuario==3):
    print("Ahora es el turno de tu rival...")
import random
numerorival= random.randint(1,3)
if numerorival==1:
    print("Tu rival seleccionó: piedra.")
elif numerorival==2:
    print("Tu rival seleccionó: papel.")
else:
     print("Tu rival seleccionó: tijera.")
   
if opcionusuario==numerorival:
     print("""
¡Casi, es un emapte!""")
if opcionusuario==1 and numerorival==2 or opcionusuario==2 and numerorival==3 or opcionusuario==3 and numerorival==1:
     print("""
Lo siento, has perdido.""")
elif opcionusuario==1 and numerorival==3 or opcionusuario==2 and numerorival==1 or opcionusuario==3 and numerorival==2:
    print("""
¡Felicidades, has ganadoooo!""")

#invocamos a la función para el segundo intento
intento_restante(intentos=2)
opcionusuario=int(input('''-Selecciona tu "arma":
          
-Presiona 1 para escoger piedra.
-Presiona 2 para escoger papel.
-Presiona 3 para escoger tijera.
'''))
if opcionusuario>3:
     print("Selecciona una opción válida por favor:")
elif (opcionusuario==1 or opcionusuario==2 or opcionusuario==3):
    print("Ahora es el turno de tu rival...")
import random
numerorival= random.randint(1,3)
if numerorival==1:
    print("Tu rival seleccionó: piedra.")
elif numerorival==2:
    print("Tu rival seleccionó: papel.")
else:
     print("Tu rival seleccionó: tijera.")

if opcionusuario==numerorival:
     print("""
¡Casi, es un emapte!""")
if opcionusuario==1 and numerorival==2 or opcionusuario==2 and numerorival==3 or opcionusuario==3 and numerorival==1:
     print("""
Lo siento, has perdido.""")
elif opcionusuario==1 and numerorival==3 or opcionusuario==2 and numerorival==1 or opcionusuario==3 and numerorival==2:
    print("""
¡Felicidades, has ganadoooo!""")
#invocamos a la función después del tercer intento
intento_restante(intentos=1)
e=("""
Creado por: Nicolás García""")
print(e)

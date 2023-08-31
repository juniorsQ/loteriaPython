#proyecto final: fundamentos básicos de python Platzi
#Apuesta de Lotería: terminales de  0-99
#Autor Juniors Quintana

import random

numerosCarton = []
numerosJugados = [0]
new_list = []
counter = 0
i = 0

while True:
  while counter < 99:
    numerosCarton.append(counter)
    counter += 1

  print("***************************************")
  print("*           Números del Carton!       *")
  print("***************************************")

  print(numerosCarton)

  print("***************************************")
  print("*           Números Jugados!          *")
  print("***************************************")

  print(new_list)
  print(len(new_list))

  if len(new_list) >= 5:
    #Si la lista de apuesta es mayor de 5 , doy la opcion de realizar el sorteo JuniorsQ
    print("***************************************")
    print("|           Realizar Sorteo!           |")
    print("***************************************")
    playSorteo = input('Desea realizar el sorteo? S/N: ')
    playSorteo = playSorteo.lower()

    if playSorteo == 's':
      numeroGanador = random.choice(numerosCarton)
      numeroGanador = str(numeroGanador)
    print("***************************************")
    print("|           Número Ganador:           |")
    print("|                  " + numeroGanador + "                  |")

    numeroGanador = int(numeroGanador)
    if numeroGanador in new_list:
      print("|           Hubo un ganador!          |")
      print("***************************************")
    else:
      print("|         No hubo un ganador!          |")
      print("***************************************")
    break

  numeroCliente = input('Indique su numero a jugar: ')
  try:
    numeroCliente = int(numeroCliente)
    if (numeroCliente > 99 or numeroCliente < 0):
      print("Número invalido!")
    elif (numeroCliente in new_list):
      print(" --------------------------------------")
      print("|     Número no disponible!            |")
      print(" --------------------------------------")
    else:
      while i <= 78:
        new_list.append(i)
        i += 1
        continue
  except ValueError:
    print("Debes escribir un número.")
  continue

import random
target = 1
roundWinC = 0
roundWinU = 0
while roundWinU <= target and roundWinC <= target :
    userOption = input('Eleccion ').title()
    option = ['Piedra','Papel','Tijera']
    computerOption = random.choice(option)
    if userOption in option:
      if userOption != computerOption:
          print(f'----------> User => {userOption} vs Maquina => {computerOption} <----------')
          if computerOption == 'Papel' and userOption != 'Tijera':
              print(f'gana Maquina con {computerOption}')
              roundWinC += 1
          elif computerOption == 'Papel' and userOption == 'Tijera':
              print(f'gana user con {userOption}')
              roundWinU += 1
          elif computerOption == 'Tijera' and userOption != 'Piedra':
              print(f'gana Maquina con {computerOption}')
              roundWinC += 1
          elif computerOption == 'Tijera' and userOption == 'Piedra':
              print(f'gana user con {userOption}')
              roundWinU += 1
          elif computerOption == 'Piedra' and userOption != 'Papel':
              print(f'gana Maquina con {computerOption}')
              roundWinC += 1
          elif computerOption == 'Piedra' and userOption == 'Papel':
              print(f'gana user con {userOption}')
              roundWinU += 1
      else:
        print('sigue Jugando misma eleccion')
    else:
      print(f'{userOption} no es una opcion del juego la opciones son {option}')
    print(f'Asi vamos Computer con {roundWinC} y User con {roundWinU}')
if roundWinU > target:
  print(f'Gana User')
elif roundWinC > target:
  print(f'Gana Maquina')


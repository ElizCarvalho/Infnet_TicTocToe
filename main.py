"""
TIC TAC TOE - Jogo da Velha com IA
"""

import random

#Globals
BOARD = dict([(idx, ' ') for idx in range(1,10)])

VICTORIES = [
	(1,2,3),
	(4,5,6),
	(7,8,9),
	(1,5,9),
	(7,5,3),
	(1,4,7),
	(2,5,8),
	(3,6,9)
]

def print_board(BOARD):
	"""
	Print the board
	"""
	print(f"{BOARD[7]}|{BOARD[8]}|{BOARD[9]}")
	print("-+-+-")
	print(f"{BOARD[4]}|{BOARD[5]}|{BOARD[6]}")
	print("-+-+-")
	print(f"{BOARD[1]}|{BOARD[2]}|{BOARD[3]}")


def has_finished():
	"""
	Check whether all available moves are made
	"""
	return  all([value != ' ' for value in BOARD.values()])


def check_sequency(positions):
	"""
	Check if a winner sequency has been filled.
	"""
	i, j, h = positions 
	if BOARD[i] == BOARD[j] == BOARD[h] != ' ':
		return True
	return False


def has_winner():
	"""
	Check whether anyone has won
	"""
	return any([check_sequency(p) for p in VICTORIES])

def reset_board():
	"""
	Clear board positions for a new round
	"""
	global BOARD
	for idx in BOARD.keys():
		BOARD[idx] = ' '

def play_human():
	"""
	Ask for human interaction
	"""
	try:
		move = int(input("Qual a posicao da sua jogada?"))
		if move not in range(1, 10):
			print("Jogada inválida. Jogue de 1 a 9")
			move = play_human()
	except ValueError:
		print("Jogada inválida. Jogue de 1 a 9")
		move = play_human()
	return move

def play_ia():
	"""
	IA pick its move
	"""
	available_moves = [positions for positions, turn in BOARD.items() if turn == ' ']
	idx = random.randint(0, len(available_moves) - 1)
	return  available_moves[idx]

PLAYERS = {
	"X": play_human, "O": play_ia
}

def game():
  global BOARD
  turn = "X"
  while not has_finished():
    #Inicia a vez
    print()
    print(f"Jogador {turn} é a sua vez.")
    
    move = PLAYERS[turn]()
    
    if BOARD[move] == ' ':
      BOARD[move] = turn
    else:
      print("Posicao já jogada.")
      continue
    
    print_board(BOARD)
    
    if has_winner():
      print("\n O JOGO ACABOU \n")
      print(f"***** {turn} ganhou *****")
      break

		#Alterna as vzs do jogo
    if turn == "X":
      turn = "O"
    else:
      turn = "X"
  
  restart = input("Gostaria de jogar novamente? (y/n)")
  if restart == "y" or restart == "Y":
    reset_board()
    game()

if __name__ == "__main__":
	game()
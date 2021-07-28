# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.words_used = []
		self.guessed_letters = [] #Lista de palavras certas
		
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word and letter not in self.guessed_letters:
			self.guessed_letters.append(letter)
		elif letter not in self.word and letter not in self.words_used:
			self.words_used.append(letter)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.words_used) == 6) #6 significa que acabou o jogo
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_'not in self.hide_word(): #Se ainda tiver um '_ ainda não acabou o jogo
			return True
		return False
		

	# Método para não mostrar a letra no board
	def hide_word(self):
		obj = ''
		for letter in self.word:
			if letter not in self.guessed_letters:
				obj += '_'
			else:
				obj += letter
		return obj

		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.words_used)]) #Acessando a lista board com len
		print('\nPalavr: ' + self.hide_word()) #retorna o underline da palavra
		print('\nLetras erradas: ',)
		for letter in self.words_used: #Para cada letra na lista de letras erradas, ele retorna a letra
			print(letter,)
		print()
		print('Letras certas: ',)
		for letter in self.guessed_letters:
			print(letter,)
		print()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines() #lê uma única linha
        return bank[random.randint(0,len(bank))].strip() #Busca uma única linha


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	

	# Verifica o status do jogo
	game.print_game_status()
	#Enquanto o jogo não terminar, solicita uma nova letra e a lê
	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

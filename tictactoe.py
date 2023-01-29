# tictaktoe.py, реализация без ООП.

import sys


ALL_SPACES = list('123456789')  # Ключи для словаря с игровым полем.
X, O, BLANK = 'X', 'O', ' '  # Константы для строковых значений.

def main():
	"""Проводит игру в крестики-нолики."""
	print('Welcome to tic-tac-toe!')
	gameBoard = getBlankBoard()  # Создать словарь с игровым полем.
	currentPlayer, nextPlayer = X, O  # X ходит первым, O ходит вторым.

	while True:
		print(getBoardStr(gameBoard))  # Вывести игровое поле на экран.

		# Запрашивать ход, пока игрок не введет число от 1 до 9:
		move = None
		while not isValidSpace(gameBoard, move):
			print(f'What is {currentPlayer}\'s move? (1-9)')
			move = input()
			if move == 'q':
				sys.exit()
		updateBoard(gameBoard, move, currentPlayer)  # Сделать ход.

		# Проверить окончание игры:
		if isWinner(gameBoard, currentPlayer):  # Сначала проверяем победу.
			print(getBoardStr(gameBoard))
			print(currentPlayer, 'has won the game!')
			break
		elif isBoardFull(gameBoard):  # Затем проверяется ничья.
			print(getBoardStr(gameBoard))
			print('The game is a tie!')
			break
		currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Передать ход.
	print('Thanks for playing!')

def getBlankBoard():
	"""Создает пустое игровое поле для игры в крестики-нолики."""
	board = {}  # Поле представляется словарем Python.
	for space in ALL_SPACES:
		board[space] = BLANK  # Все поля в исходном состоянии пусты.
	return board

def getBoardStr(board):
	"""Возвращает текстовое представление игрового поля."""
	return f'''
		{board['1']}|{board['2']}|{board['3']}  1 2 3
		-+-+-
		{board['4']}|{board['5']}|{board['6']}  4 5 6
		-+-+-
		{board['7']}|{board['8']}|{board['9']}  7 8 9
		'''

def isValidSpace(board, space):
	"""Возвращает True, если задан допустимый номер клетки, и эта клетка пуста."""
	return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
	"""Возвращает True, если игрок победил на заданном поле."""
	b, p = board, player  # Более короткие имена для удобства.
	# Проверяем 3 знака по 3 строкам, 3 столбцам и 2 диагоналям.
	return ((b['1'] == b['2'] == b['3'] == p) or  # Верхняя строка
			(b['4'] == b['5'] == b['6'] == p) or  # Средняя строка
			(b['7'] == b['8'] == b['9'] == p) or  # Нижняя строка
			(b['1'] == b['4'] == b['7'] == p) or  # Левый столбец
			(b['2'] == b['5'] == b['8'] == p) or  # Средний столбец
			(b['3'] == b['6'] == b['9'] == p) or  # Правый столбец
			(b['1'] == b['5'] == b['9'] == p) or  # Диагональ
			(b['3'] == b['5'] == b['7'] == p))  # Диагональ

def isBoardFull(board):
	"""Возвращает True, если заняты все клетки игрового поля."""
	for space in ALL_SPACES:
		if board[space] == BLANK:
			return False  # Если есть хотя бы одна пустая клетка, вернуть False.
	return True  # Пустых клеток не осталось, вернуть True.

def updateBoard(board, space, player):
	"""Заполняет клетку игрового поля знаком игрока."""
	board[space] = player

if __name__ == '__main__':
	main()	

# tictaktoe_oop.py, реализация с ООП.

import sys


ALL_SPACES = list('123456789')  # Ключи для словаря с игровым полем.
X, O, BLANK = 'X', 'O', ' '  # Константы для строковых значений.

def main():
	"""Проводит игру в крестики-нолики."""
	print('Welcome to tic-tac-toe!')
	gameBoard = TTTBoard()  # Создать объект игрового поля.
	currentPlayer, nextPlayer = X, O  # X ходит первым, O ходит вторым.

	while True:
		print(gameBoard.getBoardStr())  # Вывести игровое поле на экран.

		# Запрашивать ход, пока игрок не введет число от 1 до 9:
		move = None
		while not gameBoard.isValidSpace(move):
			print(f'What is {currentPlayer}\'s move? (1-9)')
			move = input()
			if move == 'q':
				sys.exit()
		gameBoard.updateBoard(move, currentPlayer)  # Сделать ход.

		# Проверить окончание игры:
		if gameBoard.isWinner(currentPlayer):  # Сначала проверяем победу.
			print(gameBoard.getBoardStr())
			print(currentPlayer, 'has won the game!')
			break
		elif gameBoard.isBoardFull():  # Затем проверяется ничья.
			print(gameBoard.getBoardStr())
			print('The game is a tie!')
			break
		currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Передать ход.
	print('Thanks for playing!')


class TTTBoard:
	def __init__(self, usePrettyBoard=False, useLogging=False):
		"""Создает пустое игровое поле для игры крестики-нолики."""
		self._spaces = {}  # Поле представляется словарем Python.
		for space in ALL_SPACES:
			self._spaces[space] = BLANK  # Все поля в исходном состоянии пусты.

	def getBoardStr(self):
		"""Возвращает текстовое представление игрового поля."""
		return f'''
			{self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 2 3
			-+-+-
			{self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 5 6
			-+-+-
			{self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 8 9
			'''

	def isValidSpace(self, space):
		"""Возвращает True, если задан допустимый номер клетки, и эта клетка пуста."""
		return space in ALL_SPACES and self._spaces[space] == BLANK

	def isWinner(self, player):
		"""Возвращает True, если игрок победил на заданном поле."""
		s, p = self._spaces, player  # Более короткие имена для удобства.
		# Проверяем 3 знака по 3 строкам, 3 столбцам и 2 диагоналям.
		return ((s['1'] == s['2'] == s['3'] == p) or  # Верхняя строка
				(s['4'] == s['5'] == s['6'] == p) or  # Средняя строка
				(s['7'] == s['8'] == s['9'] == p) or  # Нижняя строка
				(s['1'] == s['4'] == s['7'] == p) or  # Левый столбец
				(s['2'] == s['5'] == s['8'] == p) or  # Средний столбец
				(s['3'] == s['6'] == s['9'] == p) or  # Правый столбец
				(s['1'] == s['5'] == s['9'] == p) or  # Диагональ
				(s['3'] == s['5'] == s['7'] == p))  # Диагональ

	def isBoardFull(self):
		"""Возвращает True, если заняты все клетки игрового поля."""
		for space in ALL_SPACES:
			if self._spaces[space] == BLANK:
				return False  # Если есть хотя бы одна пустая клетка, вернуть False.
		return True  # Пустых клеток не осталось, вернуть True.

	def updateBoard(self, space, player):
		"""Заполняет клетку игрового поля знаком mark."""
		self._spaces[space] = player

if __name__ == '__main__':
	main()	

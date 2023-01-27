"""Four-in-a-Row
Игра на выстраивание четырех фишек в ряд."""

import sys

# Константы, используемые для вывода игрового поля:
EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

# Примечание: если BOARD_WIDTH изменится, обновите BOARD_TEMPLATE и COLUMN_LABELS.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# Шаблонная строка для вывода игрового поля:
BOARD_TEMPLATE = """
	 1234567 
	+-------+
	|{}{}{}{}{}{}{}|
	|{}{}{}{}{}{}{}|
	|{}{}{}{}{}{}{}|
	|{}{}{}{}{}{}{}|
	|{}{}{}{}{}{}{}|
	|{}{}{}{}{}{}{}|
	+-------+
	"""


def main():
	"""Проводит одну игру Четыре в ряд."""

	print(
		"""Four-in-a-Row

Два игрока по очереди опускают фишки в один из семи столбцов,
стараясь выстроить четыре фишки по вертикали, горизонтали или диагонали.""")

	# Подготовка новой игры:
	gameBoard = getNewBoard()
	playerTurn = PLAYER_X

	while True:  # Обрабатывает ход игрока.
		# Вывод игрового поля и получение хода игрока:
		displayBoard(gameBoard)
		playerMove = getPlayerMove(playerTurn, gameBoard)
		gameBoard[playerMove] = playerTurn

		# Проверка победы или ничьей:
		if isWinner(playerTurn, gameBoard):
			displayBoard(gameBoard)  # В последний раз вывести поле.
			print("Player {} has won!".format(playerTurn))
			sys.exit()

		elif isFull(gameBoard):
			displayBoard(gameBoard)  # В последний раз вывести поле.
			print("There is a tie!")
			sys.exit()

		# Ход передается другому игроку:
		if playerTurn == PLAYER_X:
			playerTurn = PLAYER_O
		elif playerTurn == PLAYER_O:
			playerTurn = PLAYER_X

def getNewBoard():
	"""Возвращаем словарь, представляющий игровое поле.

	Ключи - кортежи (columnIndex, rowIndex) с двумя целыми числами,
	а значения - одна из строк "X", "O" или "."."""

	board = {}
	for rowIndex in range(BOARD_HEIGHT):
		for columnIndex in range(BOARD_WIDTH):
			board[(columnIndex, rowIndex)] = EMPTY_SPACE
	return board


def displayBoard(board):
	"""Выводит на экран игровое поле и фишки."""

	# Подготовить список, передаваемый строковому методу format() для
	# шаблона игрового поля. Список содержит все фишки игрового поля
	# и пустые ячейки, перечисляемые слева направо, сверху вниз:
	tileChars = []
	for rowIndex in range(BOARD_HEIGHT):
		for columnIndex in range(BOARD_WIDTH):
			tileChars.append(board[(columnIndex, rowIndex)])

	# Выводит игровое поле:
	print(BOARD_TEMPLATE.format(*tileChars))


def getPlayerMove(playerTile, board):
	"""Предлагает игроку выбрать столбец для размещения фишки.

	Возвращает кортеж (столбец, строка) итогового положения фишки."""
	while True:
		print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} of q:")

		response = input("> ").upper().strip()
		if response == "Q":
			print("Thanks for playing!")
			sys.exit()

		if response not in COLUMN_LABELS:
			print(f"Enter a number from 1 to {BOARD_WIDTH}.")
			continue  # Снова запросить код.

		columnIndex = int(response) - 1  # -1, потому что индексы начинаются с 0.

		# Если столбец заполнен, снова запросить ход:
		if board[(columnIndex, 0)] != EMPTY_SPACE:
			print("That column is full, select another one.")
			continue  # Снова запросить ход.

		# Начать снизу, найти первую пустую ячейку:
		for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
			if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
				return (columnIndex, rowIndex)


def isFull(board):
	"""Возвращает True, если в `board` не осталось пустых ячеек,
	иначе возвращается False."""
	for rowIndex in range(BOARD_HEIGHT):
		for columnIndex in range(BOARD_WIDTH):
			if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
				return False  # Пустая ячейка найдена, вернуть False.
	return True  # Все ячейки заполнены.


def isWinner(playerTile, board):
	"""Возвращает True, если `playerTile` образует ряд из четырех фишек
	в `board`, в противном случае возвращает False."""

	# Проверить всю доску в поисках четырех фишек в ряд:
	for columnIndex in range(BOARD_WIDTH - 3):
		for rowIndex in range(BOARD_HEIGHT):
			# Проверить четверку направо:
			tile1 = board[(columnIndex, rowIndex)]
			tile2 = board[(columnIndex + 1, rowIndex)]
			tile3 = board[(columnIndex + 2, rowIndex)]
			tile4 = board[(columnIndex + 3, rowIndex)]
			if tile1 == tile2 == tile3 == tile4 == playerTile:
				return True

	for columnIndex in range(BOARD_WIDTH):
		for rowIndex in range(BOARD_HEIGHT - 3):
			# Проверить четверку вниз:
			tile1 = board[(columnIndex, rowIndex)]
			tile2 = board[(columnIndex, rowIndex + 1)]
			tile3 = board[(columnIndex, rowIndex + 2)]
			tile4 = board[(columnIndex, rowIndex + 3)]
			if tile1 == tile2 == tile3 == tile4 == playerTile:
				return True

	for columnIndex in range(BOARD_WIDTH - 3):
		for rowIndex in range(BOARD_HEIGHT - 3):
			# Проверить четверку по диагонали направо вниз:
			tile1 = board[(columnIndex, rowIndex)]
			tile2 = board[(columnIndex + 1, rowIndex + 1)]
			tile3 = board[(columnIndex + 2, rowIndex + 2)]
			tile4 = board[(columnIndex + 3, rowIndex + 3)]
			if tile1 == tile2 == tile3 == tile4 == playerTile:
				return True

			# Проверить четверку по диагонали налево вниз:
			tile1 = board[(columnIndex + 3, rowIndex)]
			tile2 = board[(columnIndex + 2, rowIndex + 1)]
			tile3 = board[(columnIndex + 1, rowIndex + 2)]
			tile4 = board[(columnIndex , rowIndex + 3)]
			if tile1 == tile2 == tile3 == tile4 == playerTile:
				return True
	return False


if __name__ == "__main__":
	main()

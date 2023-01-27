"""THE TOWER OF HANOI
Головоломка с перемещением дисков."""

import copy
import sys


TOTAL_DISKS = 5  # Чем больше дисков, тем сложнее

# Изначально все диски находятся на стрежне А:
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

num_of_moves = 0  # Подсчет количества ходов

def main():
	"""Проводит одну игру Ханойская башня."""
	print("""THE TOWER OF HANOI

Move the tower of disks, one disk at a time, to another tower.
Larger disks cannot rest on top of a smaller disk.
""")

	"""Словарь towers содержит ключи "A", "B" и "C", и значения - списки,
	представляющие стопку дисков. Список содержит целые числа, представляющие
	диски разных размеров, а начало списка представляет низ башни. Для игры
	с 5 дисками список [5, 4, 3, 2, 1] представляет заполненную башню. Пустой
	список list [] представляет башню без дисков. В списке [1, 3] больший диск
	находится на меньшем диске, такая конфигурация недопустима. Список [3, 1]
	допустим, так как меньшие диски могут размещаться на больших."""
	towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

	while True:  # Один ход для каждой итерации цикла
		# Вывести башни и диски:
		displayTowers(towers)

		# Запросить ход у пользователя
		fromTower, toTower = getPlayerMove(towers)

		# Переместить верхний диск с fromTower на toTower:
		disk = towers[fromTower].pop()
		towers[toTower].append(disk)

		# Проверить, решена ли головоломка:
		if SOLVED_TOWER in (towers["B"], towers["C"]):
			displayTowers(towers)  # Вывести башни в последний раз.
			print("You have solved the puzzle! Well done!")
			global num_of_moves
			print("Number of moves: ", num_of_moves)
			sys.exit()


def getPlayerMove(towers):
	"""Запрашивает ход у пользователя. Возвращает (fromTower, toTower)."""

	while True:  # Пока пользователь не введет допустимый ход.
		print('Enter the letters of "from" and "to" towers, or "Q".')
		print("(e.g., AB to moves a disk from tower A to tower B.)")
		global num_of_moves
		print("Number of moves:", num_of_moves)
		print()
		response = input("> ").upper().strip()

		if response == "Q":
			print("Thanks for playing!")
			sys.exit()

		# Убедитесь в том, что пользователь ввел допустимые обозначения башен:
		if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
			print("Enter one of AB, AC, BA, BC, CA, CB.")
			continue  # Снова запросить код.

		# Более содержательные имена переменных:
		fromTower, toTower = response[0], response[1]

		if len(towers[fromTower]) == 0:
			# Башня fromTower не может быть пустой:
			print("You selected a tower with no disks.")
			continue  # Снова запросить ход.
		elif len(towers[toTower]) == 0:
			num_of_moves += 1
			# На пустую башню можно переместить любой диск:
			return fromTower, toTower
		elif towers[toTower][-1] < towers[fromTower][-1]:
			print("Can't put larger disks on top of smaller ones.")
			continue  # Снова запросить ход.
		else:
			num_of_moves += 1
			# Допустимый ход, вернуть выбранные башни:
			return fromTower, toTower


def displayTowers(towers):
	"""Выводит три башни с дисками."""

	# Вывести три башни:
	for level in range(TOTAL_DISKS, -1, -1):
		for tower in (towers["A"], towers["B"], towers["C"]):
			if level >= len(tower):
				displayDisk(0)  # Вывести пустой стержень без диска.
			else:
				displayDisk(tower[level])  # Вывести диск.
		print()

	# Вывести обозначения башен A, B и C:
	emptySpace = " " * (TOTAL_DISKS)
	print("{0}A{0}{0}B{0}{0}C\n".format(emptySpace))


def displayDisk(width):
	"""Выводит диск заданной ширины. Ширина 0 означает отсутствие диска."""
	emptySpace = " " * (TOTAL_DISKS - width)

	if width == 0:
		# Вывести сегмент стержня без диска:
		print(f"{emptySpace}|{emptySpace}", end="")
	else:
		# Вывести диск:
		disk = "@" * width
		print(f"{emptySpace}{disk}{width}{disk}{emptySpace}", end="")


if __name__ == "__main__":
	main()

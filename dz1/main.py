class TicTac:
	def __init__(self):
		self.cells = [n for n in range(1, 10)]

	def show_board(self):
		for i in range(0, 7, 3):
			print(' ', self.cells[i], '│', self.cells[i + 1], '│', self.cells[i + 2])
			if i < 6:
				print(" ───┼───┼───")

	def validate_input(self, step):
		try:
			step = int(step)
		except ValueError:
			print("Вы ввели нецелое число!")
			return False
		else:
			if step > 9 or step < 1:
				print("Вы ввели неправильное число!")
				return False
			elif str(self.cells[step - 1]) not in 'X0':
				return True
			else:
				print("Данное место уже занято!")
				return False

	def start_game(self):
		print("Начало игры!")
		steps_num = 0
		win = False
		while not win:
			self.show_board()
			val = False
			while not val:
				if steps_num % 2 == 0:
					side = "X"
				elif steps_num % 2 == 1:
					side = "0"
				step = input('Куда вы хотите поставить ' + side + ':')
				val = self.validate_input(step)
				if not val:
					print("Повторите снова!")
				else:
					self.cells[int(step) - 1] = side
					val = True
			steps_num += 1
			if steps_num >= 5:
				win = self.check_winner(self.cells)
				if win:
					self.show_board()
					print("Победил " + side + '!')
					break
			if steps_num == 9:
				self.show_board()
				print("Ничья!")
				break

	def check_winner(self, cells):
		combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (2, 5, 8), (2, 4, 6), (1, 4, 7), (0, 4, 8))
		for i in combs:
			if cells[i[0]] == cells[i[1]] == cells[i[2]]:
				return f"Победил {cells[i[0]]}!"
		return False


if __name__ == '__main__':
	game = TicTac()
	game.start_game()

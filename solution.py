""" 
Максим Дрожжин
04.02.2020
Для Яндекса

Комментарии к коду в README
"""


import random
import numpy
import time

def get_alive_neighbors(grid, i, j):
    n_alive = 0
    n_alive += grid[i-1][j-1]
    n_alive += grid[i-1][j]
    n_alive += grid[i-1][j+1]
    n_alive += grid[i][j+1]
    n_alive += grid[i+1][j+1]
    n_alive += grid[i+1][j]
    n_alive += grid[i + 1][j-1]
    n_alive += grid[i][j-1]
    
    return n_alive

if __name__ == "__main__":
	random.seed(1)
	d = int(input("Нажмите 0 для ввода csv файла и 1 для случайной генерации\n"))
	m = -1
	n = -1
	grid = []

	if d == 0:
		path = input("Задайте путь к csv файлу\n")
		file_data = numpy.genfromtxt(path, delimiter=',')
		grid = numpy.pad(file_data, pad_width=1, mode='constant', constant_values=0)
		m = len(grid)
		n = len(grid[0])
		print("Изначальное поле:\n")
		print(grid[1:-1,1:-1])

	elif d == 1:
		m = int(input("Введите кол-во рядов\n")) 
		n = int(input("Введите кол-во столбцов\n")) 
		m += 2
		n += 2
		grid = []
		for i in range(m):
		    row = [0] * n
		    if i == 0 or i == (m - 1):
		        grid.append( row )
		        continue 
		    for j in range(len(row)):
		        if j == 0 or j == (n - 1):
		            row[j] = 0
		        else:
		            row[j]  = random.randint(0,1)
		    grid.append( row )
		grid = numpy.asarray(grid)
		print("Изначальное поле:\n")
		print(grid[1:-1,1:-1])

	else:
		print("Введено неверное число. Начните заново")
		exit(0)

	input("Нажмите Enter чтобы начать")

	while True:
	    for i in range(m):
	        for j in range(n):
	            if i == 0 or i == (m - 1) or j == 0 or j == (n - 1):
	                pass                           # skip if the cell is just a border cell
	            else:
	                n_alive_neighbors = get_alive_neighbors(grid, i, j)
	                if grid[i][j] == 1:            # if the cell is alive
	                    if n_alive_neighbors < 2:  # Живая клетка, у которой меньше двух живых соседей, погибает.
	                        grid[i][j] = 0
	                    if n_alive_neighbors > 3:
	                        grid[i][j] = 0         # Живая клетка, у которой больше трёх живых соседей, погибает.
	                else:                          # if the cell is dead
	                    if n_alive_neighbors == 3:
	                        grid[i][j] = 1         # Мёртвая клетка, у которой три живых соседа, возрождается.

	    print(grid[1:-1,1:-1])
	    print("\n")
	    time.sleep(1)



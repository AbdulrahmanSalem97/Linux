from os import system, name
from time import sleep

def clear():
        _ = system('cls')
 
while True:
	for i in range(10):
		print("\t\t\t\t\t\n",end="")
	for i in range(5):
		print("\t\t\t\t\t\t",end="")
		for k in range (i+1):
			print("*",end="")
		print("")
	print("\t\t\t\t\t",end="")
	for i in range(17):
		print("*",end="")
	print("")	
	for i in range(5, 0, -1):
		print("\t\t\t\t\t\t",end="")
		for j in range(0, i):
			print("*", end="")
		print("")
	sleep(0.4)
	clear()
	for i in range(15):
		print("\t\t\t\t\t\n",end="")
	for i in range(8):
		print("\t\t\t\t\t*")
	for i in range(5, 1, -1):
		print("\t\t\t\t  ",end="")
		for space in range(0, 5-i):
			print("  ", end="")
		for j in range(i, 2*i-1):
			print("* ", end="")
		for j in range(1, i-1):
			print("* ", end="")
		print()
	sleep(0.4)
	clear()
	for i in range(10):
		print("\t\t\t\t\t\n",end="")
	for i in range(5):
		print("\t\t\t  ",end="")
		for j in range(6 - i - 1):
			print(' ', end='')
		# print stars
		for k in range(i + 1):
			print('*', end='')
		print()
	print("\t\t\t",end="")
	for i in range(17):
		print("*",end="")
	print(" ")
	for i in range(6 - 1):
		print("\t\t\t  ",end="")
		for j in range(i + 1):
			print(' ', end='')
		# print stars
		for k in range(6 - i - 1):
			print('*', end='')
		print()
	sleep(0.4)
	clear()
	
	for i in range(5):
		print("\t\t\t\t\t\n",end="")
	k = 0
	for i in range(1, 4+1):
		for space in range(-14,(6-i)+1):
			print(end="  ")
		while k!=(2*i-1):
			print("* ", end="")
			k += 1
		k = 0
		print()
		
	for i in range(8):
		print("\t\t\t\t\t*")
	print(" ")
	sleep(0.4)
	clear()
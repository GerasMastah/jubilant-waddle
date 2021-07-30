import os
from tabulate import tabulate
from apis import *
from functions import bcolors

os.system('cls||clear')

print(f"{bcolors.HEADER}Que API deseas utilizar?{bcolors.ENDC} \n {bcolors.OKCYAN}1.- ipstack  \n 2.- ipapi \n 3.- Salir{bcolors.ENDC}")

while True:
	try:
		choice = int(input(""))
		
		if choice == 1:
			os.system('cls||clear')
			print(f"{bcolors.OKBLUE}Haz Elegido ipstack \n{bcolors.ENDC}")
			print(tabulate(ipstack_API(),tablefmt='grid'))

			print(f"{bcolors.HEADER}Que API deseas utilizar?{bcolors.ENDC} \n {bcolors.OKCYAN}1.- ipstack  \n 2.- ipapi \n 3.- Salir{bcolors.ENDC}")
			

		elif choice == 2:
			os.system('cls||clear')
			print(f"{bcolors.OKBLUE}Haz Elegido ipapi \n{bcolors.ENDC}")
			os.system('cls||clear')
			print(tabulate(ipapi_API(),tablefmt='grid'))

			print(f"{bcolors.HEADER}Que API deseas utilizar?{bcolors.ENDC} \n {bcolors.OKCYAN}1.- ipstack  \n 2.- ipapi \n 3.- Salir{bcolors.ENDC}")

		elif choice == 3:
			break
			

		else:
			print(f"{bcolors.OKBLUE}Elige una opcion Valida{bcolors.ENDC}")
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass
	pass
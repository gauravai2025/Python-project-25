#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passw2=[]    #empty list
passw3=" "
for i in range(0,nr_letters):
  passw2+=letters [random.randint(0,51)]
for i in range(0,nr_symbols):
  passw2+=symbols  [random.randint(0,8)]
  # pass+=random.choice(symbols) 
for i in range(0,nr_numbers):
 passw2+=numbers  [random.randint(0,9)]
total=nr_letters+nr_symbols+nr_numbers
random.shuffle(passw2)
for u in passw2:
  passw3+=u
print(f'your strong password is {passw3}')
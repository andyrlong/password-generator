import random 

print("Welcome to your password generator: ")

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Length of your password: ")
length = int(length)

print("\nYour passwords: ")

for pwd in range(number):
    passwords = ''

for c in range(length):
    passwords += random.choice(chars)
    print(passwords)
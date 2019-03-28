import os

print("Welcome to my AI Pacman Program")
print("Here are my four level of pacman")
print("1. Level 1 \n\
2. Level 2 \n\
3. Level 3 \n\
4. Level 4\n")

choice = input("Please choose a level you want to see from the list above: ")
if choice == "A":
    os.system("Level1.py")
elif choice == "B":
    os.system("Level1.py")

else:
    print("Sorry that has not been found. Please enter 1, 2, 3, 4")
    exit()  
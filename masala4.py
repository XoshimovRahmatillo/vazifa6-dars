import os

new_papka = input("Yangi papka nomini kiriting: ")


os.chdir(new_papka)

new_papka = os.getcwd()
print(f"O'zgargan ishchi papka: {new_papka}")

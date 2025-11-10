import os

folders = input("Enter folder names :- ").split()

for folder in folders:

    try:
        list_folder = os.listdir(folder)
        print(list_folder)

    except FileNotFoundError:
        print(f'Folder "{folder}" do not exist ')

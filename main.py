from lib.file_handling import *
from lib.front_menus import *
from time import sleep


# check/create data
data_users = "data_users.txt"
data_contacts = "data_contacts.txt"
exist(data_users)
exist(data_contacts)

# check/create main user

#iniciar no usuario principal
print("\n\n")
home_menu(data_users, data_contacts)

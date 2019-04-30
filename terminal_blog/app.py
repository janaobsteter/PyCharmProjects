from database import Database
from menu import Menu
from modules.blog import Blog


Database.initialise() #this created Database.DATABASE


menu = Menu()
menu.run_menu()

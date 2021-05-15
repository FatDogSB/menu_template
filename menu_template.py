import argparse
import sys
import os
import shutil
import datetime
import sabnzb
import re
import sqlite3

menu_actions = {}

#-------------------------------------------------------------------------------
def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-keep_days_back', 	nargs=1, required=True, type = int, help='Number of days of files to keep', default=30)
	parser.add_argument('-pattern', 		nargs=1, required=True, type=str, 	help='File pattern to use')
	parser.add_argument('-path',			nargs=1, required=True, type=str, 	help='Path to folder with old files')
	
	# No input means we should print the help message
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit()
		
	return parser.parse_args()
	

	
#-------------------------------------------------------------------------------
def menu_folder_rename():
	print ('Clean Sabnsb Folders starting...')
	base_path = 'D:\\temp\\SabNZB\\output'

	obj = sabnzb.sabnzb(base_path)

	# Run through folders and delete empty ones
	obj.remove_unwanted_folders()

	# Run through folders and find url/sfv/etc file extensions we do not want and delete them
	obj.fix_obfuscated_foldernames()


#-------------------------------------------------------------------------------
# Main Menu
#-------------------------------------------------------------------------------
def main_menu():
 
	os.system('cls')
	
	print ("Welcome,")
	print ("Please choose the menu item:")
	print ("1 . ")
	print ("2 . ")
	print ("3 . ")
	print ("4 . ")
	print ("5 . ")
	print ("6 . ")
	print ("7 . ")
	print ("8 . ")
	print ("9 . ")
	print ("10. ")
	print ("11. ")
	print ("0 . Quit")
	choice = input(" >> ")
	exec_menu(choice)
	
	return
	

#-------------------------------------------------------------------------------
def exec_menu(choice):
	os.system('cls')
	ch = choice.lower()
	print ('Choice: {0}'.format(ch))
	if ch == '':
		menu_actions['main_menu']()
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print ("Invalid selection, please try again.")
			menu_actions['main_menu']()
	return



#-------------------------------------------------------------------------------
def menu_scan_for_files():
	print ("Scan for files starting...")


	return

#-------------------------------------------------------------------------------
def not_implimented():
	print ("Sorry, this option is not implimented")
	
def back():
	menu_actions['main_menu']()
def exit():
	sys.exit()
#-------------------------------------------------------------------------------
# This structure links menu choices to functions.
menu_actions = {
	'main_menu' : main_menu,
	'1' : menu_folder_rename,
	'2' : not_implimented,
	'3' : not_implimented,
	'4' : not_implimented,
	'5' : not_implimented,
	'6' : not_implimented,
	'7' : not_implimented,
	'8' : not_implimented,
	'9' : not_implimented,
	'10': not_implimented,
	'11': not_implimented,
	'0' : exit,
}


if __name__ == '__main__':
	# Launch main menu
	main_menu()


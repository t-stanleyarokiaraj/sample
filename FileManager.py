# !/usr/bin/python

import os
from os.path import join, getsize

Options = input('Enter any of the below Options\n\
G - To generate the list file\n\
C - To copy the required files\n\
D - To remove the marked duplicates\n\
: ')

MasterPath = input('Enter the root path: ')

Language = {
			'ENG':'English',
			'TAM':'Tamil',
			'TEL':'Telugu',
			'MAL':'Malayalam',
			'KAN':'Kanada'
			}

Genre = {
		'ACT':'Action',
		'ADV':'Adventure',
		'COL':'Collection/Saga',
		'COM':'Comedy',
		'CRI':'Crime',
		'DRA':'Drama',
		'FAN':'Fantasy',
		'FIC':'Fiction',
		'HIS':'Historical',
		'HOR':'Horror',
		'MYS':'Mystery',
		'PHI':'Philosophical',
		'POL':'Political',
		'ROM':'Romance',
		'SOC':'Social',
		'THR':'Thriller'
		}

def GenerateList():
	FilePointer = open(MasterPath+'\FileList.txt','w')

	for root, folder, files in os.walk(MasterPath):
		root = root.split('\\')
		#filePointer.write(root + ' consumes ' + str(sum([getsize(join(root, name)) for name in files])) + ' bytes in ' + str(len(files)) + ' non-directory files\n')
		if not folder:
			#FilePointer.write(root[len(root)-1] + '\t\t does not have any subfolder\n')
			if (root[len(root)-3] in list(Language.values()) and root[len(root)-2] in list(Genre.values())):
				try:
					FilePointer.write('X' + ':' + list(Language.keys())[list(Language.values()).index(root[len(root)-3])] + ':' + \
									 list(Genre.keys())[list(Genre.values()).index(root[len(root)-2])] + ':' + \
									 root[len(root)-1])
				except:
					continue
				#FilePointer.write(root[len(root)-3] + '\t\t' + root[len(root)-2] + '\t\t' + root[len(root)-1] + '\n')  #+ '\t\t' + str(files)
				#continue
		elif root[len(root)-1] not in folder: #root and folder name should not be same.
			#FilePointer.write(root[len(root)-1] + '\t\t' + str(folder) + '\n')  #+ '\t\t' + str(files) 
			continue
	FilePointer.close()
	
if Options.upper() == 'G':
	GenerateList()

import os
from os import listdir
from os.path import isfile, join, splitext, exists, isdir

folderVar = '/mnt/c/Users/jackb/Downloads'
os.chdir(folderVar)
onlyFiles = [ f for f in listdir(folderVar) if isfile(join(folderVar, f))]

if(len(onlyFiles) > 0):
	for file in onlyFiles:
		folder = splitext(file)[1][1:]

		if(not exists(join(folderVar, folder.upper()))):
			os.makedirs(folder.upper())
			print('[Folder] ' + folder.upper() + ' folder is created.')

		os.rename(join(folderVar, file), join(join(folderVar, folder.upper()) , file))
		print('[File] ' + file + ' is moved to ' + join(folderVar, folder.upper()))
else:
	print('You folder is already clean.')


	





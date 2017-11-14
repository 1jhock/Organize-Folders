import os
from os import listdir
from os.path import isfile, join, splitext, exists, isdir


folderVar = '/mnt/c/Users/jackb/Desktop/python-projects/sample'
os.chdir(folderVar)
onlyfiles = [ f for f in listdir(folderVar) if isfile(join(folderVar, f))]


for file in onlyfiles:
	folder = splitext(file)[1][1:]


	if(not exists(join(folderVar, folder.upper()))):
		os.makedirs(folder.upper())
		print(folder.upper() + ' folder is created')

	os.rename(join(folderVar, file), join(join(folderVar, folder.upper()) , file))
	print(file + ' is moved to ' + join(folderVar, folder.upper()))

	





from datetime import datetime
from pathlib import Path
import os
import getPath
import folderizer
from record import getData

filePath = getPath.getPath()
print(filePath.parent)
name_of_file = input("What is the name of the list: ")
completeName = os.path.join(filePath, name_of_file+".txt")
file1 = open(completeName, "w")

numberOfFiles = input("How many files would you like to process?")

# set for loop for 'numberOfFiles'

for file in filePath.iterdir():
    if file.name != '.DS_Store' and file.is_file():
        data = getData(file)
        file1.write(f'{data} \n')
        # file path is NOT where .place() saves the file
        destination = folderizer.place(file, filePath)
        # 'destination' should be the new folder path for the file
        file1.write(f'@{destination} \n')

file1.close()

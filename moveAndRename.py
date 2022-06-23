from datetime import datetime
from msilib.schema import Directory
import os
from tkinter import N
from getPath import getPath
from pathlib import Path
import shutil


filePath = getPath()
fileParent = filePath.parent
new_path = getPath()

for file in filePath.iterdir():
    if file.name != '.DS_Store' and file.is_file():
        extension = file.suffix
        old_name = file.stem

        N = old_name.split('-')
        nameStem = N[-1]
        print(nameStem)

        new_name = f'{nameStem}{extension}'

        new_file_path = new_path.joinpath(new_name)
        print(new_file_path)

        shutil.move(filePath.joinpath(file.name), new_file_path)

        # F:\Archives\Mass\2018\06\08
        # F:\Archives\Mass

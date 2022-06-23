from datetime import datetime
from msilib.schema import Directory
import os
from getPath import getPath
from pathlib import Path
import shutil


filePath = getPath()
fileParent = filePath.parent


for file in filePath.iterdir():
    if file.name != '.DS_Store' and file.is_file():
        extension = file.suffix
        old_name = file.stem

        dc = datetime.fromtimestamp(
            os.path.getmtime(file)).strftime("%Y-%m-%d")
        Ye, Mo, Da = dc.split('-')

        new_path = filePath.joinpath(Ye).joinpath(Mo).joinpath(Da)
        print(new_path)
        if os.path.isdir(new_path) == False:
            os.makedirs(new_path)

        new_name = f'{Ye}-{Mo}-{Da}-{old_name}{extension}'
        print(new_name)

        new_file_path = new_path.joinpath(new_name)

        shutil.move(filePath.joinpath(file.name), new_file_path)

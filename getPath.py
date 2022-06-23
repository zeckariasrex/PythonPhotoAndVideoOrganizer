from pathlib import Path
from importlib.resources import path
from os import scandir


def getPath():
    pathIn = input("Please enter Path:")

    print(pathIn)
    if pathIn[0] == '"':
        if pathIn[-1] == '"':
            pathIn = pathIn[1:-1]
        else:
            pathIn = pathIn[1:]
    else:
        if pathIn[-1] == '"':
            pathIn = pathIn[:-1]
    print(pathIn)

    filePath = Path(pathIn)

    with scandir(filePath) as itr:

        if filePath.is_dir():
            print(" is a directory.")
            return filePath
        else:
            print(" is not a directory.")
            getPath()


# uncomment to debug file
# getPath()
# print(filePath)

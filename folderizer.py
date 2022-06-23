
from curses import window
import datetime
from logging.config import _LoggerConfiguration
import shutil


def place(file, filePath):

    dc = datetime.fromtimestamp(
        file.stat().st_ctime).strftime("%Y-%m-%d")
    dc_os = datetime.fromtimestamp(
        os.path.getctime(file)).strftime("%Y-%m-%d")

    Ye, Mo, Da = dc.split('-')
    Yea, Mont, Das = dc_os.split('-')

    Year = min(Ye, Yea)
    Month = min(Mo, Mont)
    Day = min(Da, Das)

    new_Name_String = f'/{Year}/{Month}/{Day}'
    tyPe = file.suffix[1:]
   foldeaPath = os.path.join(filePath.parent, f'{Year}\{Month}\{Day}\{tyPe}')

    shutil.move(file,)

    if type == IMG or VID:  # open custom window preview with taging and file name entry
        openPreviewTagger()

       # file2.open() with markdown including imaage link at new file location
       # append tags with obsidian formating and description


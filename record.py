

import datetime
import os


def getData(file):

    if file.name != '.DS_Store':
        dty = file.parent
        ext = file.suffix

        old_name = file.stem
        date_created = file.stat().st_ctime
        date_created_os = os.path.getctime(file)

        dc_conv = datetime.fromtimestamp(
            date_created).strftime("%d-%B-%Y")
        dc_os_conv = datetime.fromtimestamp(
            date_created_os).strftime("%d-%B-%Y")
        toFile = f'{old_name}, {dc_conv}, OS {dc_os_conv}'
        return toFile

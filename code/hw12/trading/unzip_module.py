from zipfile import ZipFile


def unzip_file(file_name) -> str:
    my_zip = ZipFile(file_name, mode="r")
    for files in my_zip.namelist():
        print(files, "--> exctracting...")
        my_zip.extract(files)
    return file_name[0:len(file_name)-4]

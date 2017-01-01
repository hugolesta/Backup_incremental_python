import glob
import os


class So:
    pass

class Folder:

    def set_directory(self,directory):
        self.directory = directory
        return directory


class File(Folder,So):

    def __init__(self,directory,extension):
        self.extension = self.set_extension(extension)
        self.directory = self.set_directory(directory)

    def set_extension(self,extension):
        self.extension = extension
        return  extension

    def buscar_archivos(self,directory,extension):
        os.chdir(directory)
        archivos = glob.glob(extension)
        for i in range(len(archivos)):
            print(archivos[i])




import glob
import os


class Directorio(object):
  def __init__(self, directory, extension):
    self.extension = extension
    self.directory = directory

    def archivos(self):
      directory = self.directory  # obtienes el directorio desde el __init__
      extension = self.extension  # obtienes la extension desde el __init__
      os.chdir(directory)
      archivos = glob.glob(extension)
      return archivos  # retorna la lista creada

    def zipdir(self,direcory,ziph):
      import zipfile
      for root, dirs, files in os.walk(direcory):
        for file in files:
          ziph.write(os.path.join(root,file))

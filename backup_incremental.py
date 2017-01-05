from clases_main import Directorio
import shutil,zipfile
from datetime import date

directorio = 'D:/script_bk'
extension = '**'

# Objeto de Instancia
search_archivos = Directorio(directorio, extension)

# for archivo in search_archivos.archivos():
#     shutil.copy(archivo)

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    search_archivos.zipdir(directorio,zipf)
    zipf.close()
    print(date.today())
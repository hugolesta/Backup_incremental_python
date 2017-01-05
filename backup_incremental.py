from clases_main import Directorio
import shutil,zipfile
import time
import datetime

directorio = 'D:/script_bk'
directorio_destino = 'C:/Users/Hnl22/Desktop/Python/scripts/move-files/'
extension = '**'
fechahora= time.strftime("%Y-%m-%d-%H-%M-%S")
# Objeto de Instancia
search_archivos = Directorio(directorio, extension)

# for archivo in search_archivos.archivos():
#     shutil.copy(archivo)

if __name__ == '__main__':
    zipf = zipfile.ZipFile(directorio_destino+'bk-'+fechahora+'.zip', 'w', zipfile.ZIP_DEFLATED)
    search_archivos.zipdir(directorio,zipf)
    zipf.close()

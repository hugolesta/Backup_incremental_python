from clases_main import Directorio
import shutil,zipfile
import time
import datetime

directorio = 'E:/script_bk/'
directorio_destino = 'E:/script_bk/'
extension = '**'
fechahora= time.strftime("%Y-%m-%d-%H-%M-%S")
# Objeto de Instancia
search_archivos = Directorio(directorio, extension)

# for archivo in search_archivos.archivos():
#     shutil.copy(archivo)

if __name__ == '__main__':
  if directorio == directorio_destino:
  	print("El directorio principal no debe ser igual al directorio donde se guardarán los Backups")
  else:
  	zipf = zipfile.ZipFile(directorio_destino+'bk-'+fechahora+'.zip', 'w', zipfile.ZIP_DEFLATED)
  	search_archivos.zipdir(directorio,zipf)
  	zipf.close()

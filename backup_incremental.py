
from clases_main import File

directorio = 'D:/'
extension = '*.txt'

# Objeto de Instancia
search_archivos = File(directorio,extension)


search_archivos.buscar_archivos(directorio,extension)

# Importamos las librerias necesarias
from os import listdir, path, walk, stat
from mimetypes import MimeTypes
import pymysql
# Realizamos la conexion
conexion = pymysql.connect(host="localhost",user="factura",password="2125",db="patrimonio")
# Realizamos el for en el directorio deseado
# este recorre todas las subcarpetas que contenga
for raiz, d, f in walk("/media/seiyukaras/Karas/Videos/musicales"):
	# creamos otro for para listar los elementos del directorio
	for elementos in listdir(raiz):
		# Asignamos el nombre del elemento a la variable name
		name = elementos
		# Creamos la ruta completa del elemento
		pathinf = raiz + "/" + name
		# Obtenemos el tipo del Videos
		mime = MimeTypes()
		type = mime.guess_type(pathinf)[0]
		# Consultamos el tipo del archivo
		# Cualquier formato que sea del tipo video, pasara
		if 'video' in str(type):
			# Obtenemos el tamaño del video
			tamanio = stat(pathinf).st_size
			# Consultamos el tamaño y lo configuramos segun el mismo
			if tamanio <= 1024:
				sigla = "byte"
			elif tamanio <= 1048576:
				sigla = "Kb"
				tamanio = round((tamanio / 1024),1)
			elif tamanio <= 1073741824:
				sigla = "Mb"
				tamanio = round((tamanio / 1048576),1)
			elif tamanio <= 1099511627776:
				sigla = "Gb"
				tamanio = round((tamanio / 1073741824),1)
			# Creamos las variables para insertar en la db
			nombre = (str(raiz + "/" + name))
			peso = (str(tamanio) + sigla)
			# Probamos la consulta
			with conexion.cursor() as cursor:
				# Damos formato a la consulta
				sql = ("insert into buscar_buscar(fichero,tamanno) "
                        "values('" + nombre +"','" + peso + "');")
				try:
					# Intentamos ejecutar
					cursor.execute(sql)
				except:
					# Mensaje error
					print("Error al insertar los datos")
			# Enviamos la query
			conexion.commit()
# Cerramos la conexion
conexion.close()
print("Finalizado exitosamente")
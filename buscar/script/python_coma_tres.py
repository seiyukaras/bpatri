# Importamos las librerias necesarias
from os import listdir, path, walk, stat
from mimetypes import MimeTypes
# Abrimos o creamos el txt para escribir los textos
txt = open('videos.txt', 'w')

# Realizamos el for en el directorio deseado
# este recorre todas las subcarpetas que contenga
for raiz, d, f in walk("/media/seiyukaras/Karas"):
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
		if 'video' in str(type):
			# Obtenemos el tamaño del video
			tamanio = stat(pathinf).st_size
			# Consultamos el tamaño y lo configuramos segun el mismo
			if tamanio >= 1024:
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
				# Imprime la ruta del video y el tamaño del mismo
				texto = (str(name + " * " + raiz + " * " + str(type) + " * " + str(tamanio) + sigla))
				txt.write(texto + "\n")
txt.close()

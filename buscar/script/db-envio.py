from buscar.models import buscar
fichero = open('/media/seiyukaras/Karas/Proyectos/bpatri/buscar/script/videos.txt', 'r', encoding='utf-8')
for linea in fichero.readlines():
    dato = linea.split(',')
    registro, created = buscar.objects.get_or_create(fichero=dato[0].strip().encode('utf-8'))
    registro.tamanno = dato[1].strip()
    registro.nombre = dato[2].strip()
    registro.save()


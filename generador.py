import os
import glob
#leer archivos 
titleO = open("titulo.txt", "r")
descO = open("descripcion.txt", "r")
campoO = open("campo3.txt", "r")
titleR = titleO.read()
descR = descO.read()
campoR = campoO.read()
titleO.close()
campoO.close()
descO.close()

#imprimir en pantalla
# print(titleR)
# print(descR)
# print(campoR)

#Obteniendo path de imagen
path = glob.glob('*.jpg', recursive = False)
path += glob.glob('*.png', recursive = False)
path += glob.glob('*.gif', recursive = False)
imagenes = ''
for nombre in path:
    imagenes += '<img src="'+nombre+'" alt="">'

print(imagenes)
#Generando HTML
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>P&aacutegina de productos</title>
</head>
<body>
    <p>"""+titleR+"""</p>
    <p>"""+descR+"""</p>
    <p>"""+campoR+"""</p>
    """+imagenes+"""
</body>
</html>"""

pagina = open('./generador.html', 'w')
pagina.write(html)
pagina.close
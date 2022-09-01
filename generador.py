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

#Obteniendo path de imagenes con diferentes extensiones
path = glob.glob('*.jpg', recursive = False)
path += glob.glob('*.png', recursive = False)
path += glob.glob('*.gif', recursive = False)
path += glob.glob('*.webp', recursive = False)
path += glob.glob('*.jfif', recursive = False)

imagenes = ''
divImagenes = ''
slide = 0
for nombre in path:
    slide= slide +1
    imagenes += """<img src=\""""+nombre+"""\" alt="imagen"""+str(slide)+"""\" onclick="openModal();currentSlide("""+str(slide)+""")">
                """
    divImagenes += """<div class="mySlides">
                        <div class="numbertext"></div>
                        <img src=\""""+nombre+"""\" style="width:100%">
                    </div>"""      

#print(imagenes)
#print(divImagenes)
#Generando HTML
html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galer&iacutea</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100;200;400;500&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <h1>"""+titleR+"""</h1>
    </header>
    <main>
        <div class="imagenes">
        """+imagenes+"""
        </div>

        <!-- The Modal/Lightbox -->
        <div id="myModal" class="modal">
        <span class="close cursor" onclick="closeModal()">&times;</span>
        <div class="modal-content">
            """+divImagenes+"""
            <!-- Next/previous controls -->
            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>
        </div>
        </div>

        <aside>
        <div class="info">
            <div class="titulo">
            <p>"""+descR+"""</p>
            </div>

            <div class="opc">
            <div class="precio">
                <p>"""+campoR+"""</p>
            </div>
    
            <div class="comprar">
                <button type="button" onclick="comprar()">Comprar</button>
            </div>
            </div>

        </div>
        </aside>


    </main>
    <script src="./src/main.js"></script>
    
</body>
</html>"""

pagina = open('./generador.html', 'w')
pagina.write(html)
pagina.close
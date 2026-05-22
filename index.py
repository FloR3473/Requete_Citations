# Requeter API




# Traduire API (trier les informations que l'on souhaite garder)



# Produire un fichier HTML
with open("index.html", mode= "w", encoding="utf-8", newline="") as web:
    web.write('<!DOCTYPE HTML>')
    web.write('<HTML lang="FR">')
    web.write('    <head>')
    web.write('        <meta charset="utf-8">')
    web.write('        <title> Requête citations </title>')
    web.write('         <link href="style.css" rel="stylesheet" >')
    web.write('          <h1>Citations<h1>')
    web.write('     </head>')
    web.write('     <body>')
    web.write('         ')
    web.write('    </body>')
    web.write('</HTML>')

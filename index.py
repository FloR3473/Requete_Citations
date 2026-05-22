import requests
import html

# Requeter API
i= 0
citations = []

for i in range(5):
    response = requests.get("http://api.quotable.io/random")
    data = response.json()
    citations.append((data['content'],data['author']))

# print(citations)

# Traduire API (trier les informations que l'on souhaite garder)



# Produire un fichier HTML
# print (citations)
with open("index.html", mode= "w", encoding="utf-8", newline="") as web:
    web.write('<!DOCTYPE HTML>\n')
    web.write('<HTML lang="FR">\n')
    web.write('    <head>\n')
    web.write('        <meta charset="utf-8">\n')
    web.write('        <title> Requête citations </title>\n')
    web.write('         <link href="style.css" rel="stylesheet" >\n')
    web.write('            <h1> Citations </h1>')
    web.write('     </head>\n')
    web.write('     <body>\n')
    for i in range(5) :
         
         web.write(f'<div><p>{citations[i][0]} </p>')
         web.write(f'<p>{citations[i][1]} </p></div>')
    web.write('    </body>\n')
    web.write('</HTML>\n')
    
    

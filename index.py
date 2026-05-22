import requests
import html

# Requeter API
citations = []

for i in range(5):
    response = requests.get("http://api.quotable.io/random")
    data = response.json()
    citations.append((data['content'],data['author']))

print(citations)

# Traduire API (trier les informations que l'on souhaite garder)



# Produire un fichier HTML




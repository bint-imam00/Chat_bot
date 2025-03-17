      
import requests
from bs4 import BeautifulSoup
import os
import time

# Créer les dossiers nécessaires
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)

# URL de base
base_url = "https://cfptsj.sn/"

# Liste des pages à visiter
pages = [
    "", "formations/", "partenaires/", "admission/", "a-propos-de-nous/", 
    "contact/",  "actualites/"
]

all_content = []

for page in pages:
    url = base_url + page
    print(f"Récupération de {url}...")
    
    try:
        # Ajouter des en-têtes pour simuler un navigateur
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extraire tous les contenus textuels significatifs
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li', 'div', 'span']):
            text = tag.get_text(strip=True)
            if text and len(text) > 3:  # Ignorer les textes trop courts
                # Formatter le texte avec le type de tag
                tag_name = tag.name
                formatted_text = f"[{tag_name.upper()}] {text}"
                all_content.append(formatted_text)
        
        # Chercher les liens vers d'autres pages pertinentes
        if page == "formations/":
            for link in soup.find_all('a', href=True):
                href = link['href']
                if 'formation' in href.lower() and href.startswith('/') and href not in pages:
                    subpage = href.lstrip('/')
                    if subpage not in pages:
                        pages.append(subpage)
        
        # Respecter le site en ajoutant un délai entre les requêtes
        time.sleep(1)
        
    except Exception as e:
        print(f"Erreur lors de la récupération de {url}: {e}")

# Filtrer et nettoyer le contenu
filtered_content = []
for text in all_content:
    if text.strip() and len(text.strip()) > 3:
        filtered_content.append(text)

# Supprimer les doublons
unique_content = list(dict.fromkeys(filtered_content))

response.encoding = 'utf-8'  
# Sauvegarder le contenu
with open("data/cfptsj_data.txt", "w", encoding="utf-8") as f:
    for line in unique_content:
        f.write(line + "\n\n")  # Double saut de ligne pour séparer les passages

print(f"Données récupérées avec succès ! {len(unique_content)} passages uniques extraits.")
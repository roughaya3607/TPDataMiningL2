import pandas as pd
import requests
from bs4 import BeautifulSoup

# ===========================
# Exercice 1 : JSON + Excel
# ===========================

# JSON
films = pd.read_json("movies.json")
print("=== Données des films ===")
print(films)

# Excel
donnees_excel = pd.read_excel("data.xlsx")
print("\n=== Données Excel ===")
print(donnees_excel)

# ===========================
# Exercice 2 : CSV étudiants
# ===========================

etudiants = pd.read_csv("student_performance.csv")

# Vérifier que la colonne "G3" existe
if "G3" in etudiants.columns:
    etudiants_filtres = etudiants[etudiants["G3"] > 15]
    print("\n=== Étudiants avec G3 > 15 ===")
    print(etudiants_filtres)
else:
    print("Erreur : la colonne 'G3' n'existe pas dans le fichier CSV")

# ===========================
# Exercice 3 : Web Scraping + API
# ===========================

# Web Scraping
url_scraping = "https://books.toscrape.com"
robots = requests.get(url_scraping + "/robots.txt")
print("\n=== robots.txt ===")
print(robots.text)

response = requests.get(url_scraping)
soup = BeautifulSoup(response.text, "html.parser")
titres = soup.find_all("h3")
print("\n=== Titres sur la page ===")
for t in titres:
    print(t.text)

# API
url_api = "https://jsonplaceholder.typicode.com/posts"
response_api = requests.get(url_api)
data_api = pd.DataFrame(response_api.json())
print("\n=== Données de l'API ===")
print(data_api.head())
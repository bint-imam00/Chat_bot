# Utiliser une image Python officielle
FROM python:3.9

# Définir le répertoire de travail à la racine du projet
WORKDIR /app

# Copier tous les fichiers dans l'image Docker
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000
EXPOSE 8000

# Lancer l'API avec Uvicorn
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]

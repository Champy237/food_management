# # Utilise une image officielle de Python
# FROM python:3.12-slim

# # Définit le répertoire de travail
# WORKDIR /app

# # Copie les fichiers nécessaires
# COPY requirements.txt /app/

# # Installation des dépendances
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --upgrade pip



# # Définit la variable d'environnement pour Flask
# ENV FLASK_APP=flask/run.py
# ENV FLASK_ENV=development


# # Copie tout le contenu du projet
# COPY . .

# # Expose le port sur lequel Flask tourne
# EXPOSE 5000

# # Démarre l’application
# CMD ["python", "run.py"]

# Utiliser une image Python slim officielle
FROM python:3.12-slim

WORKDIR /app

# Mettre à jour pip avant l'installation
RUN pip install --upgrade pip

# Copier requirements.txt et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers
COPY . .

# Variables d'environnement Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

EXPOSE 5000

# Démarrer l'application
CMD ["python", "run.py"]

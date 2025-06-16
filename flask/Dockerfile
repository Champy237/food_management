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

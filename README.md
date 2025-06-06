# food_management
Projet Flask de Gestion Alimentaire
Description
Ce projet est une application backend développée avec Flask, SQLAlchemy et PostgreSQL.
Elle permet de gérer des utilisateurs, des consommateurs, des nourritures, des ingrédients, ainsi que leurs relations comme les allergies et l'historique de consommation.

Fonctionnalités
Gestion des utilisateurs (inscription, identification, etc.)

Gestion des consommateurs liés aux utilisateurs

Gestion des nourritures et catégories associées

Gestion des ingrédients pour chaque nourriture

Suivi des allergies des consommateurs

Historique de consommation avec suivi des effets (malaise, etc.)

Technologies utilisées
Python 3.12

Flask (micro-framework web)

SQLAlchemy (ORM pour la base de données)

PostgreSQL (base de données relationnelle)

psycopg2 (connecteur PostgreSQL pour Python)

Installation
Cloner le dépôt :

bash
Copy
Edit
git clone <URL_DU_DEPOT>
cd <NOM_DU_REPO>
Créer un environnement virtuel Python et l’activer :

bash
Copy
Edit
python3 -m venv virtuel
source virtuel/bin/activate  # Linux/Mac
# virtuel\Scripts\activate   # Windows
Installer les dépendances :

bash
Copy
Edit
pip install -r requirements.txt
Configurer la base de données PostgreSQL :

Créer la base db_food

Configurer les identifiants dans le fichier de configuration Flask (config.py ou .env)

Exemple de configuration :

env
Copy
Edit
DATABASE_URL=postgresql://champy:AZERTY2005@localhost/db_food
Initialiser la base de données (création des tables) :

bash
Copy
Edit
flask db upgrade  # si tu utilises Flask-Migrate
# ou exécuter un script d'initialisation
Lancer l’application :

bash
Copy
Edit
flask run
Utilisation
L’application expose des routes API REST (exemple: /utilisateurs, /consommateurs, /nourritures, etc.)

Tu peux utiliser Postman ou curl pour tester les endpoints.

Un exemple d’insertion via shell Python avec SQLAlchemy est fourni dans le dossier /scripts.

Structure du projet
bash
Copy
Edit
/app
  /models.py          # Modèles SQLAlchemy
  /routes.py          # Routes Flask
  /services.py        # Logique métier
  /repository.py      # Accès aux données
/config.py            # Configuration Flask et base de données
/run.py               # Point d’entrée de l’application
/requirements.txt     # Dépendances Python
/README.md            # Ce fichier
Contribuer
Forker le projet

Créer une branche (git checkout -b feature/ma-feature)

Commit tes modifications (git commit -m 'Ajout de ma feature')

Push la branche (git push origin feature/ma-feature)

Ouvrir une Pull Request

Licence
Ce projet est sous licence MIT.

Si tu veux, je peux aussi te générer un exemple de fichier requirements.txt ou un fichier .env exemple.
Veux-tu ?

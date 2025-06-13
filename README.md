# Nutrition Manager API

Une API RESTful développée avec **Flask** pour gérer des données nutritionnelles : consommateurs, ingrédients, aliments, catégories, allergies,historiques de consommation et la gestion des chartbot dans domain de la nutrition. Le projet vise des applications comme la **gestion de plans alimentaires**, **buffets**, ou **suivi nutritionnel intelligent**.

## Fonctionnalités

* Authentification et gestion des utilisateurs
* Gestion des consommateurs
* Gestion des aliments, ingrédients, catégories, allergies et chaetbot
* Historique de consommation
* Gestion du chartbot
* Architecture (Model - Repository - Service - Route)
* Dockerisé pour un déploiement rapide

## Architecture du projet

```
flask/
|── app/
    |── static/           # fichier static des images
        |── uploads/      # stocker les images 
    |── models.py         # Modèles SQLAlchemy (Utilisateur, Nourriture, etc.)
    |── repositories.py   # Opérations CRUD bas niveau
    |── services.py       # Logique métier
    |── routes.py         # Endpoints API Flask (users.py, consommateur.py, etc.)
    |── __init__.py       # Initialisation de l'application Flask
|── config.py             # Configuration (base de données, .env)
|── docker-compose.yml
|── Dockerfile            
|── .env                  # configuration des cle api
|── .venv/                # environement virtuel


```

---

## Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/Champy237/FOOD_MANAGEMENT.git
cd flask
```

### 2. Créer un environnement virtuel

```bash
cd flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurer les variables d’environnement

```
OPENROUTER_API_KEY=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
GOOGLE_API_KEY=AIzaSyCOFaTg8zwm52DoFwzqIjjTn5xebiSaHqQ
DEEPSEEK_API_KEY=sk-b4eca66ce49345e8af6c381a9ae2fff2
DATABASE_URL=postgresql://champy:AZERTY2005@localhost:5432/db_food
```

### 4. Lancer l'application

```bash
flask run
# ou
python run.py

docker compose up --build
```

---

##  Lancer avec Docker

```bash
docker compose up --build
```
---

## Test de l'API avec Postman

Tous les endpoints sont testables via **Postman**. Assurez-vous que le serveur est bien démarré à l'adresse :  
📍 `http://localhost:5000/`

###  Utilisateur

| Méthode| Endpoint                | Description                      |
|--------|-------------------------|----------------------------------|
| POST   | `api/users/register`    | Enregistrer un utilisateur       |
| POST   | `api/users/login`       | Connexion utilisateur            |
| GET    | `api/users/`            | Lister les utilisateurs          |

###  Consommateur

| Méthode| Endpoint                      | Description                      |
|--------|-------------------------------|----------------------------------|
| GET    | `api/consommateurs/`          | Lister les consommateurs         |
| POST   | `api/consommateurs/`          | Ajouter un consommateur          |
| GET    | `api/consommateurs/<id>`      | Voir un consommateur             |
| PUT    | `api/consommateurs/<id>`      | Mettre à jour un consommateur    |
| DELETE | `api/consommateurs/<id>`      | Supprimer un consommateur        |



###  Nourriture

| Méthode | Endpoint                | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `api/liste_nuritures/`   | Lister les nourritures           |
| POST   | `api/nourritures/`       | Ajouter une nourriture           |
| GET    | `api/nourritures/<id>`   | Voir une nourriture              |
| PUT    | `api/nourritures/<id>`   | Modifier une nourriture          |
| DELETE | `api/nourritures/<id>`   | Supprimer une nourriture         |

###  Ingrédients

| Méthode| Endpoint                 | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `api/liste_ingredients/` | Lister les ingrédients           |
| POST   | `api/ingredients/`       | Ajouter un ingrédient            |
| GET    | `api/ingredients/<id>`   | Voir un ingrédient               |
| PUT    | `api/ingredients/<id>`   | Modifier un ingrédient           |
| DELETE | `api/ingredients/<id>`   | Supprimer un ingrédient          |

###  Catégories

| Méthode| Endpoint                 | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `api/liste_categories/`  | Lister les catégories            |
| POST   | `api/categories/`        | Ajouter une catégorie            |
| GET    | `api/categories/<id>`    | Voir une catégorie               |
| PUT    | `api/categories/<id>`    | Modifier une catégorie           |
| DELETE | `api/categories/<id>`    | Supprimer une catégorie          |

###  Allergies

| Méthode| Endpoint                 | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `api/liste_alergies/`    | Lister les allergies             |
| POST   | `api/alergies/`          | Ajouter une allergie             |
| GET    | `api/alergies/<id>`      | Voir une allergie                |
| PUT    | `api/alergies/<id>`      | Modifier une allergie            |
| DELETE | `api/alergies/<id>`      | Supprimer une allergie           |

###  Historique de consommation

| Méthode | Endpoint                | Description                            |
|--------|--------------------------|----------------------------------------|
| GET    | `api/liste_historiques/` | Lister les historiques                 |
| POST   | `api/historiques/`       | Enregistrer une consommation           |
| GET    | `api/historiques/<id>`   | Détails d’un historique                |
| DELETE | `api/historiques/<id>`   | Supprimer un historique                |


### Chart bot 
| Méthode | Endpoint                | Description                            |
|--------|--------------------------|----------------------------------------|
| GET    | `api/chartbot/`          | discusion avec un chartbot             |





## Exemple de requête (Postman)

### Ajouter une nourriture

```json
POST /nourritures/
Content-Type: application/json

{
  "nom": "Riz",
  "categorie_id": 1
}
```

---

## 🧪 Tests

Les tests se font via **Postman**. Une collection peut être ajoutée dans `/postman/` si besoin.

---

## 📦 Technologies utilisées

* Python 3.12
* Flask
* SQLAlchemy
* PostgreSQL
* Docker / Docker Compose
* psycopg2
* requestes

---

## Licence

Ce projet est sous licence **MIT**. Voir le fichier [`LICENSE`](./LICENSE) pour plus d'informations.

---

© 2025 Champy. Tous droits réservés.

![Licence MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)

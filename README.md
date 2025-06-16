# Nutrition Manager API

Une API RESTful développée avec **Flask** pour gérer des données nutritionnelles : consommateurs, ingrédients, aliments, catégories, allergies, historiques de consommation et la gestion des chatbot dans le domaine de la nutrition. Le projet vise des applications comme la **gestion de plans alimentaires**, **buffets**, ou **suivi nutritionnel intelligent**.

## Fonctionnalités

* Authentification et gestion des utilisateurs
* Gestion des consommateurs
* Gestion des aliments, ingrédients, catégories, allergies et chatbot
* Historique de consommation
* Gestion du chatbot
* Architecture (Model - Repository - Service - Route)
* Dockerisé pour un déploiement rapide

## Architecture du projet

```
flask/
|── app/
    |── static/           # fichiers statiques des images
        |── uploads/      # stockage des images 
    |── models.py         # Modèles SQLAlchemy (Utilisateur, Nourriture, etc.)
    |── repositories.py   # Opérations CRUD bas niveau
    |── services.py       # Logique métier
    |── routes.py         # Endpoints API Flask (users.py, consommateur.py, etc.)
    |── __init__.py       # Initialisation de l'application Flask
|── config.py             # Configuration (base de données, .env)
|── docker-compose.yml
|── Dockerfile            
|── .env                  # configuration des clefs API
|── .venv/                # environnement virtuel
```

---

## Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/Champy237/food_management.git
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

## Lancer avec Docker

```bash
docker compose up --build
```

---

## Test de l'API avec Postman

Tous les endpoints sont testables via **Postman**. Assurez-vous que le serveur est bien démarré à l'adresse :  
`http://localhost:5000/`

---

## Routes pour les `Utilisateurs`

### Mettre à jour un utilisateur

- **Méthode**: PUT  
- **URL**: `http://127.0.0.1:5000/api/utilisateurs/1`
- **Headers**:
  - `Content-Type: application/json`
- **Body (JSON)**:
```json
{
  "nom": "NouveauNom",
  "email": "nouveau@email.com"
}
```
- **Réponse attendue**:
```json
{
  "id": 1,
  "nom": "NouveauNom",
  "email": "nouveau@email.com"
}
```

---

### Supprimer un utilisateur

- **Méthode**: DELETE  
- **URL**: `http://127.0.0.1:5000/api/utilisateurs/1`
- **Réponse attendue**: Code HTTP `204 No Content`

---

## Routes pour les `Consommateurs`

### Ajouter des ingrédients prédéfinis

- **Méthode**: POST  
- **URL**: `http://127.0.0.1:5000/api/populate_ingredients`
- **Réponse attendue**:
```json
{
  "message": "5 ingrédients ajoutés.",
  "ingredients": [...]
}
```

---

### 👤 Créer un consommateur

- **Méthode**: POST  
- **URL**: `http://127.0.0.1:5000/api/consommateurs`
- **Headers**:
  - `Content-Type: application/json`
- **Body**:
```json
{
  "nom": "Jean Dupont",
  "email": "jean@example.com"
}
```
- **Réponse attendue**: Le consommateur créé avec son `id`

---

### Lister tous les consommateurs

- **Méthode**: GET  
- **URL**: `http://127.0.0.1:5000/api/liste_consommateurs`
- **Réponse attendue**:
```json
[
  {
    "id": 1,
    "nom": "Jean Dupont",
    "email": "jean@example.com"
  },
  ...
]
```

---

### Obtenir un consommateur par ID

- **Méthode**: GET  
- **URL**: `http://127.0.0.1:5000/api/consommateurs/1`

---

### 🛠️ Modifier un consommateur

- **Méthode**: PUT  
- **URL**: `http://127.0.0.1:5000/api/consommateurs/1`
- **Headers**:
  - `Content-Type: application/json`
- **Body**:
```json
{
  "nom": "Jean Modifié",
  "email": "modifie@example.com"
}
```

---

### 🗑️ Supprimer un consommateur

- **Méthode**: DELETE  
- **URL**: `http://127.0.0.1:5000/api/consommateurs/1`
- **Réponse attendue**: Code HTTP `204 No Content`

---

##  Nourritures

### Récupérer toutes les nourritures

- **Méthode**: GET  
- **URL**: `http://localhost:5000/nuritures`

---

### Récupérer une nourriture par ID

- **Méthode**: GET  
- **URL**: `http://localhost:5000/nuritures/1`

---

### Récupérer nourritures avec catégories

- **Méthode**: GET  
- **URL**: `http://localhost:5000/liste_nuritures`

---

### Créer une nouvelle nourriture (avec image)

- **Méthode**: POST  
- **URL**: `http://localhost:5000/nuritures`  
- **Type**: form-data  
- **Params**:
  - `nom`: Riz au poulet
  - `description`: Plat pakistanais traditionnel
  - `type`: plat principal
  - `prix`: 12.5
  - `image`: fichier image (type file)

---

### Modifier une nourriture

- **Méthode**: PUT  
- **URL**: `http://localhost:5000/nuritures/1`  
- **Type**: JSON  
- **Body**:
```json
{
  "nom": "Riz basmati",
  "description": "Riz parfumé au safran",
  "type": "accompagnement",
  "prix": 7.5,
  "image_url": "http://url-de-l-image"
}
```

---

### Supprimer une nourriture

- **Méthode**: DELETE  
- **URL**: `http://localhost:5000/nuritures/1`

---

## Ingrédients

- GET `/ingredients` : Liste tous les ingrédients.
- GET `/ingredients/<id>` : Détail d’un ingrédient.
- POST `/ingredients` : Créer un ingrédient (JSON).
- PUT `/ingredients/<id>` : Modifier un ingrédient (JSON).
- DELETE `/ingredients/<id>` : Supprimer un ingrédient.

---

##  Catégories

- GET `/categories` : Liste des catégories.
- GET `/categories/<id>` : Détail d'une catégorie.
- POST `/categories` : Créer une catégorie (JSON).
- PUT `/categories/<id>` : Modifier une catégorie (JSON).
- DELETE `/categories/<id>` : Supprimer une catégorie.

---

## 🔗 Association Nourriture ↔Catégorie

- POST `/nuriture_categorie` : Associer une nourriture à une catégorie (JSON).
- DELETE `/nuriture_categorie` : Supprimer une association (JSON).
- POST `/nuritures/<nuriture_id>/categories/<categorie_id>` : Même fonction, plus RESTful.
- DELETE `/nuritures/<nuriture_id>/categories/<categorie_id>` : Supprimer la catégorie via URL.

---

##  Historique de consommation

### Créer un historique

- **Méthode**: POST  
- **URL**: `http://localhost:5000/historique/`  
- **Body (JSON)**:
```json
{
  "consommateur_id": 1,
  "nuriture_id": 3,
  "a_eu_malaise": true
}
```
- **Réponse**:
```json
{
  "id": 10,
  "consommateur_id": 1,
  "nuriture_id": 3,
  "a_eu_malaise": true
}
```

---

### Vérification d’allergie

- **Méthode**: GET  
- **URL**: `http://localhost:5000/historique/allergie?consommateur_id=1&nuriture_id=3`
- **Réponse**:
```json
{
  "allergie_probable": true
}
```

---

##  Chatbot

### Poser une question

- **Méthode**: POST  
- **URL**: `http://localhost:5000/chatbot`  
- **Body (JSON)**:
```json
{
  "question": "Quels sont les ingrédients du couscous ?"
}
```
- **Réponse**:
```json
{
  "réponse": "Le couscous contient généralement de la semoule, des légumes, et de la viande."
}
```

---

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

##  Tests

Les tests se font via **Postman**. Une collection peut être ajoutée dans `/postman/` si besoin.

---

##  Technologies utilisées

* Python 3.12
* Flask
* SQLAlchemy
* PostgreSQL
* Docker / Docker Compose
* psycopg2
* requests

---

## Licence

Ce projet est sous licence **MIT**. Voir le fichier [`LICENSE`](./LICENSE) pour plus d'informations.

---

© 2025 Champy. Tous droits réservés.

![Licence MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)
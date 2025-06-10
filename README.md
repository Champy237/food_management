# 🥗 Nutrition Manager API

Une API RESTful développée avec **Flask** pour gérer des données nutritionnelles : consommateurs, ingrédients, aliments, catégories, allergies et historiques de consommation. Le projet vise des applications comme la **gestion de plans alimentaires**, **buffets**, ou **suivi nutritionnel intelligent**.

## 🚀 Fonctionnalités

* 🔐 Authentification et gestion des utilisateurs
* 🧍 Gestion des consommateurs
* 🧂 Gestion des aliments, ingrédients, catégories et allergies
* 🗓️ Historique de consommation
* 📦 Architecture modulaire (Model - Repository - Service - Route)
* 🐳 Dockerisé pour un déploiement rapide

## 🧱 Architecture du projet

```
app/
├── models/         # Modèles SQLAlchemy (Utilisateur, Nourriture, etc.)
├── repositories/   # Opérations CRUD bas niveau
├── services/       # Logique métier
├── routes/         # Endpoints API Flask (users.py, consommateur.py, etc.)
├── config/         # Configuration (base de données, .env)
├── __init__.py     # Initialisation de l'application Flask
```

---

## 🛠️ Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/Champy237/FOOD_MANAGEMENT.git
cd flask
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurer les variables d’environnement

Modifier `.env` si nécessaire :

```
DATABASE_URL=postgresql://champy:AZERTY2005@localhost:5432/db_food
```

### 4. Lancer l'application

```bash
flask run
# ou
python run.py
```

---

## 🐳 Lancer avec Docker

```bash
docker-compose up --build
```

---

## 📫 Test de l'API avec Postman

Tous les endpoints sont testables via **Postman**. Assurez-vous que le serveur est bien démarré à l'adresse :  
📍 `http://localhost:5000/`

### 🔐 Utilisateur

| Méthode | Endpoint             | Description                     |
|--------|----------------------|----------------------------------|
| POST   | `/users/register`    | Enregistrer un utilisateur       |
| POST   | `/users/login`       | Connexion utilisateur            |
| GET    | `/users/`            | Lister les utilisateurs          |

### 👤 Consommateur

| Méthode | Endpoint              | Description                     |
|--------|-----------------------|----------------------------------|
| GET    | `/consommateurs/`     | Lister les consommateurs         |
| POST   | `/consommateurs/`     | Ajouter un consommateur          |
| GET    | `/consommateurs/<id>` | Voir un consommateur             |
| PUT    | `/consommateurs/<id>` | Mettre à jour un consommateur    |
| DELETE | `/consommateurs/<id>` | Supprimer un consommateur        |

### 🍎 Nourriture

| Méthode | Endpoint              | Description                     |
|--------|-----------------------|----------------------------------|
| GET    | `/nourritures/`       | Lister les nourritures           |
| POST   | `/nourritures/`       | Ajouter une nourriture           |
| GET    | `/nourritures/<id>`   | Voir une nourriture              |
| PUT    | `/nourritures/<id>`   | Modifier une nourriture          |
| DELETE | `/nourritures/<id>`   | Supprimer une nourriture         |

### 🧂 Ingrédients

| Méthode | Endpoint              | Description                     |
|--------|-----------------------|----------------------------------|
| GET    | `/ingredients/`       | Lister les ingrédients           |
| POST   | `/ingredients/`       | Ajouter un ingrédient            |
| GET    | `/ingredients/<id>`   | Voir un ingrédient               |
| PUT    | `/ingredients/<id>`   | Modifier un ingrédient           |
| DELETE | `/ingredients/<id>`   | Supprimer un ingrédient          |

### 📁 Catégories

| Méthode | Endpoint              | Description                     |
|--------|-----------------------|----------------------------------|
| GET    | `/categories/`        | Lister les catégories            |
| POST   | `/categories/`        | Ajouter une catégorie            |
| GET    | `/categories/<id>`    | Voir une catégorie               |
| PUT    | `/categories/<id>`    | Modifier une catégorie           |
| DELETE | `/categories/<id>`    | Supprimer une catégorie          |

### ⚠️ Allergies

| Méthode | Endpoint              | Description                     |
|--------|-----------------------|----------------------------------|
| GET    | `/alergies/`          | Lister les allergies             |
| POST   | `/alergies/`          | Ajouter une allergie             |
| GET    | `/alergies/<id>`      | Voir une allergie                |
| PUT    | `/alergies/<id>`      | Modifier une allergie            |
| DELETE | `/alergies/<id>`      | Supprimer une allergie           |

### 🗓️ Historique de consommation

| Méthode | Endpoint              | Description                           |
|--------|-----------------------|----------------------------------------|
| GET    | `/historiques/`       | Lister les historiques                 |
| POST   | `/historiques/`       | Enregistrer une consommation           |
| GET    | `/historiques/<id>`   | Détails d’un historique                |
| DELETE | `/historiques/<id>`   | Supprimer un historique                |

---

## ✅ Exemple de requête (Postman)

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

---

## 📜 Licence

Ce projet est sous licence **MIT**. Voir le fichier [`LICENSE`](./LICENSE) pour plus d'informations.

---

© 2025 Champy. Tous droits réservés.

![Licence MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)

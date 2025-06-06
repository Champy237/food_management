# 🥗 Nutrition Manager API

Une API RESTful développée avec **Flask** pour gérer des données nutritionnelles, des consommateurs, des ingrédients, des aliments et des historiques de consommation. Ce projet est destiné à des applications dans la **gestion de plans alimentaires**, **buffets**, ou **suivi nutritionnel intelligent**.

## 🚀 Fonctionnalités

* 🔐 Authentification et gestion des utilisateurs
* 🢑 Gestion des consommateurs
* 🍎 Gestion des aliments et catégories
* 🠂 Ingrédients et composition des plats
* 🗓️ Historique de consommation
* 📦 Architecture modulaire (Model - Repository - Service - Route)
* 🐳 Dockerisé pour un déploiement rapide

## 🧱 Architecture

```
app/
├── models/         # Modèles SQLAlchemy
├── repositories/   # Requêtes DB (CRUD)
├── services/       # Logique métier
├── routes/         # Endpoints Flask
├── config/         # Configuration
├── __init__.py     # Initialisation Flask
```

## 🛠️ Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-utilisateur/nutrition-manager.git
cd nutrition-manager
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration

Modifier les variables d’environnement dans `.env` si nécessaire (notamment pour PostgreSQL) :

```
DATABASE_URL=postgresql://champy:AZERTY2005@localhost:5432/db_food
```

### 4. Lancer l'application

```bash
flask run
```

## 🐳 Utilisation avec Docker

```bash
docker-compose up --build
```

## 📦 Technologies utilisées

* Python 3.12
* Flask
* SQLAlchemy
* PostgreSQL
* Docker / Docker Compose
* psycopg2

## 📄 API Endpoints

| Ressource    | Méthode | Endpoint          | Description                      |
| ------------ | ------- | ----------------- | -------------------------------- |
| Utilisateur  | `POST`  | `/users/register` | Créer un utilisateur             |
| Consommateur | `GET`   | `/consommateurs/` | Lister les consommateurs         |
| Nourriture   | `POST`  | `/nourritures/`   | Ajouter une nourriture           |
| Ingrédient   | `GET`   | `/ingredients/`   | Voir les ingrédients disponibles |
| Historique   | `POST`  | `/historiques/`   | Enregistrer une consommation     |

## ✅ Exemple de requête

```bash
curl -X POST http://localhost:5000/nourritures/ \
  -H "Content-Type: application/json" \
  -d '{"nom": "Riz", "categorie_id": 1}'
```

## 🧪 Tests

```bash
pytest
```

## 📜 Licence

Ce projet est sous licence **MIT**. Voir le fichier [`LICENSE`](./LICENSE) pour plus d'informations.

---

© 2025 Champy. Tous droits réservés.

---

![Licence MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)


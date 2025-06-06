# 🥗 Projet Flask - API de Gestion Alimentaire

Ce projet est une API RESTful développée avec Flask pour la gestion des utilisateurs, des consommateurs, des nourritures, des ingrédients, des allergies et de l’historique de consommation.

## 🚀 Fonctionnalités

- Création et gestion des utilisateurs
- Association d’un consommateur à un utilisateur
- Création et consultation de nourritures et de leurs catégories
- Définition des ingrédients pour chaque nourriture
- Suivi des allergies d’un consommateur
- Enregistrement de l’historique de consommation et détection de malaises

## 🛠️ Technologies

- **Python 3.12**
- **Flask**
- **SQLAlchemy**
- **PostgreSQL**
- **psycopg2**
- Architecture : `models/`, `repositories/`, `services/`, `routes/`

## 🧱 Structure du Projet

```
.
├── app/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── routes/
│   └── __init__.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. **Cloner le projet**
```bash
git clone <url_du_repo>
cd <nom_du_projet>
```

2. **Créer un environnement virtuel**
```bash
python -m venv virtuel
source virtuel/bin/activate  # Linux/Mac
# virtuel\Scripts\activate  # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer PostgreSQL**

Créer la base de données PostgreSQL `db_food` :

```bash
psql -U champy -c "CREATE DATABASE db_food;"
```

Configurer `config.py` ou `.env` :

```
DATABASE_URL=postgresql://champy:AZERTY2005@localhost/db_food
```

5. **Lancer le projet**
```bash
python run.py
```

## 🧪 Utilisation

Tu peux utiliser Postman, curl ou Swagger pour interagir avec l’API :

- `POST /utilisateurs` – Créer un utilisateur
- `GET /nourritures` – Liste des nourritures
- `POST /historique` – Ajouter une consommation
- `GET /consommateur/<id>/allergies` – Allergies d’un consommateur

## 📥 Peuplement de la base (exemple shell Python)

```python
from app.models.utilisateur import Utilisateur
from app import db

user = Utilisateur(nom="Ali", prenom="Khan", email="ali.khan@example.com", password="motdepasse")
db.session.add(user)
db.session.commit()
```

## ✅ TODO

- Ajouter l’authentification JWT
- Ajouter Swagger UI ou Redoc pour la doc API
- Ajouter des tests unitaires

## 📄 Licence

Ce projet est sous licence MIT. Tu es libre de l’utiliser et de le modifier.

---

🎯 *Développé avec passion pour apprendre les architectures backend avec Flask et PostgreSQL.*

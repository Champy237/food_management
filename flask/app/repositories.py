from app import db
from app.models import Consommateur, Nuriture, Ingredient, Categorie,HistoriqueConsommation
from sqlalchemy import func
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = "app/static/images"
from flask import url_for, current_app
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UtilisateurRepository:
    def __init__(self):
        from app.models import Utilisateur
        self.model = Utilisateur

    def list_utilisateurs(self): 
        return self.model.query.all()

    def get_utilisateurs(self):
        return self.model.query.all()

    def get_utilisateur(self, id):
        return self.model.query.get(id)

    def create_utilisateur(self, data):
        utilisateur = self.model(**data)
        from app import db
        db.session.add(utilisateur)
        db.session.commit()
        return utilisateur

    def update_utilisateur(self, id, data):
        utilisateur = self.model.query.get(id)
        if not utilisateur:
            return None
        for key, value in data.items():
            setattr(utilisateur, key, value)
        from app import db
        db.session.commit()
        return utilisateur

    def delete_utilisateur(self, id):
        utilisateur = self.model.query.get(id)
        if not utilisateur:
            return False
        from app import db
        db.session.delete(utilisateur)
        db.session.commit()
        return True



class ConsommateurRepository:
    def create_consommateur(self, data):
        consommateur = Consommateur(nom=data["nom"], email=data["email"])
        db.session.add(consommateur)
        db.session.commit()
        return consommateur
    
    def list_consommateurs(self):
        return Consommateur.query.all()
    

    def get_by_nom(self, nom: str):
        return db.session.query(Consommateur).filter_by(nom=nom).first()


    def get_consommateur_by_id(self, consommateur_id):
        return Consommateur.query.get(consommateur_id)

    def update_consommateur(self, consommateur_id, data):
        consommateur = self.get_consommateur_by_id(consommateur_id)
        if consommateur:
            consommateur.nom = data.get("nom", consommateur.nom)
            consommateur.email = data.get("email", consommateur.email)
            db.session.commit()
        return consommateur

    def delete_consommateur(self, consommateur_id):
        consommateur = self.get_consommateur_by_id(consommateur_id)
        if consommateur:
            db.session.delete(consommateur)
            db.session.commit()
        return consommateur



class NuritureRepository:
    def create_nuriture(self, data, file=None):
        image_url = None

        # Gestion du fichier image
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Crée le dossier s'il n'existe pas
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            image_url = f"/static/images/{filename}"

        nuriture = Nuriture(
            nom=data["nom"],
            description=data.get("description"),
            type=data.get("type"),
            prix=data.get("prix"),
            image_url=image_url
        )

        # Récupération des catégories
        if "categories" in data:
            import json
            categories_ids = json.loads(data["categories"]) if isinstance(data["categories"], str) else data["categories"]
            categories = Categorie.query.filter(Categorie.id.in_(categories_ids)).all()
            nuriture.categories = categories

        db.session.add(nuriture)
        db.session.commit()
        return nuriture
    
    def get_by_nom(self, nom: str):
        return db.session.query(Nuriture).filter_by(nom=nom).first()
    

    def list_nuritures(self):
        return Nuriture.query.all()
 
    def get_nuriture_by_id(self, nuriture_id):
        return Nuriture.query.get(nuriture_id)

    def update_nuriture(self, nuriture_id, data, file=None):
        nuriture = self.get_nuriture_by_id(nuriture_id)  # méthode à créer pour récupérer par id
        if nuriture:
            nuriture.nom = data.get("nom", nuriture.nom)
            nuriture.description = data.get("description", nuriture.description)
            nuriture.type = data.get("type", nuriture.type)
            nuriture.prix = data.get("prix", nuriture.prix)

            if "categories" in data:
                categories = Categorie.query.filter(Categorie.id.in_(data["categories"])).all()
                nuriture.categories = categories

            if file:
                from werkzeug.utils import secure_filename
                import os

                filename = secure_filename(file.filename)
                filepath = os.path.join('static/images', filename)
                file.save(filepath)
                nuriture.image_url = '/' + filepath  # adapter selon config Flask

            db.session.commit()
        return nuriture

    def delete_nuriture(self, nuriture_id):
        nuriture = self.get_nuriture_by_id(nuriture_id)
        if nuriture:
            db.session.delete(nuriture)
            db.session.commit()
        return nuriture



class IngredientRepository:
    def create_ingredient(self, data):
        ingredient = Ingredient(nom=data["nom"], description=data.get("description"))
        db.session.add(ingredient)
        db.session.commit()
        return ingredient

    def get_by_nom(self, nom):
        return Ingredient.query.filter_by(nom=nom).first()
    

    def list_ingredients(self):
        return Ingredient.query.all()

    def get_ingredient_by_id(self, ingredient_id):
        return Ingredient.query.get(ingredient_id)

    def update_ingredient(self, ingredient_id, data):
        ingredient = self.get_ingredient_by_id(ingredient_id)
        if ingredient:
            ingredient.nom = data.get("nom", ingredient.nom)
            ingredient.description = data.get("description", ingredient.description)
            db.session.commit()
        return ingredient

    def delete_ingredient(self, ingredient_id):
        ingredient = self.get_ingredient_by_id(ingredient_id)
        if ingredient:
            db.session.delete(ingredient)
            db.session.commit()
        return ingredient



class CategorieRepository:
    def create_categorie(self, data):
        categorie = Categorie(nom=data["nom"])
        db.session.add(categorie)
        db.session.commit()
        return categorie

    def get_by_nom(self, nom):
        return Categorie.query.filter_by(nom=nom).first()

    def list_categories(self):
        return Categorie.query.all()

    def get_categorie_by_id(self, categorie_id):
        return Categorie.query.get(categorie_id)

    def update_categorie(self, categorie_id, data):
        categorie = self.get_categorie_by_id(categorie_id)
        if categorie:
            categorie.nom = data.get("nom", categorie.nom)
            db.session.commit()
        return categorie

    def delete_categorie(self, categorie_id):
        categorie = self.get_categorie_by_id(categorie_id)
        if categorie:
            db.session.delete(categorie)
            db.session.commit()
        return categorie



class NuritureCategorieRepository:
    
    def create_nuriture_categorie(self, nuriture_id, categorie_ids):
        """
        Lie une Nuriture à plusieurs catégories.
        nuriture_id : int
        categorie_ids : list d'entiers
        """
        nuriture = Nuriture.query.get(nuriture_id)
        if not nuriture:
            return None  # ou lever une erreur

        # Récupère les catégories demandées
        categories = Categorie.query.filter(Categorie.id.in_(categorie_ids)).all()
        if not categories:
            return None  # ou lever une erreur
        
        # Associe les catégories à la nourriture
        nuriture.categories = categories
        
        db.session.commit()
        return nuriture

    def get_nuriture_categories(self):
        """
        Retourne toutes les nourritures avec leurs catégories.
        """
        return Nuriture.query.all()

    def get_nuriture_categorie(self, id):
        """
        Retourne une nourriture par son id avec ses catégories.
        """
        return Nuriture.query.get(id)

    def delete_nuriture_categorie(self, nuriture_id):
        """
        Supprime une nourriture (et ses liens catégories par cascade).
        """
        nuriture = Nuriture.query.get(nuriture_id)
        if not nuriture:
            return False
        
        db.session.delete(nuriture)
        db.session.commit()
        return True

    def add_categorie_to_nuriture(self, nuriture_id, categorie_id):
        """
        Ajoute une catégorie à une nourriture existante.
        """
        nuriture = Nuriture.query.get(nuriture_id)
        categorie = Categorie.query.get(categorie_id)
        if not nuriture or not categorie:
            return False
        
        if categorie not in nuriture.categories:
            nuriture.categories.append(categorie)
            db.session.commit()
        return True

    def remove_categorie_from_nuriture(self, nuriture_id, categorie_id):
        """
        Enlève une catégorie d'une nourriture.
        """
        nuriture = Nuriture.query.get(nuriture_id)
        categorie = Categorie.query.get(categorie_id)
        if not nuriture or not categorie:
            return False
        
        if categorie in nuriture.categories:
            nuriture.categories.remove(categorie)
            db.session.commit()
        return True



class HistoriqueConsommationRepository:
    def create_historique(self, data):
        historique = HistoriqueConsommation(
            consommateur_id=data["consommateur_id"],
            nuriture_id=data["nuriture_id"],
            a_eu_malaise=data.get("a_eu_malaise", False)  #
        )
        db.session.add(historique)
        db.session.commit()
        return historique

    def detecter_allergie_probable(self, consommateur_id, nuriture_id):
        total = HistoriqueConsommation.query.filter_by(
            consommateur_id=consommateur_id,
            nuriture_id=nuriture_id
        ).count()

        malaises = HistoriqueConsommation.query.filter_by(
            consommateur_id=consommateur_id,
            nuriture_id=nuriture_id,
            a_eu_malaise=True
        ).count()

        if total == 0:
            return False  # Pas assez de données

        taux = (malaises / total) * 100
        return taux >= 30


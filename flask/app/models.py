
from app import db
from datetime import datetime



nuriture_categorie = db.Table(
    'nuriture_categorie',
    db.Column('nuriture_id', db.Integer, db.ForeignKey('nuriture.id'), primary_key=True),
    db.Column('categorie_id', db.Integer, db.ForeignKey('categorie.id'), primary_key=True)
)

consommateur_allergie = db.Table(
    'consommateur_allergie',
    db.Column('consommateur_id', db.Integer, db.ForeignKey('consommateur.id'), primary_key=True),
    db.Column('nuriture_id', db.Integer, db.ForeignKey('nuriture.id'), primary_key=True)
)


class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "email": self.email,
        }



class Consommateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)


    allergies = db.relationship(
        'Nuriture',
        secondary=consommateur_allergie,
        backref='consommateurs_allergiques'
    )


    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "email": self.email
        }

class Nuriture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    type = db.Column(db.String(50))
    prix = db.Column(db.Float)
    image_url = db.Column(db.String(255)) 
    categories = db.relationship('Categorie', secondary=nuriture_categorie, backref='nuritures')
    

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "type": self.type,
            "prix": self.prix,
            "image_url": self.image_url,
            "categories": [c.to_dict() for c in self.categories],
        }

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description
        }

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom
        }


class HistoriqueConsommation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consommateur_id = db.Column(db.Integer, db.ForeignKey('consommateur.id'), nullable=False)
    nuriture_id = db.Column(db.Integer, db.ForeignKey('nuriture.id'), nullable=False)
    a_eu_malaise = db.Column(db.Boolean, nullable=False)

    consommateur = db.relationship('Consommateur', backref='consommations')
    nuriture = db.relationship('Nuriture', backref='consommations')

    def to_dict(self):
        return {
            "id": self.id,
            "consommateur_id": self.consommateur_id,
            "nuriture_id": self.nuriture_id,
            "a_eu_malaise": self.a_eu_malaise
        }


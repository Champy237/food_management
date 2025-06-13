import os
import requests
from dotenv import load_dotenv

from app.repositories import UtilisateurRepository
from app.repositories import ConsommateurRepository
from app.repositories import NuritureRepository
from app.repositories import IngredientRepository
from app.repositories import NuritureCategorieRepository
from app.repositories import HistoriqueConsommationRepository


class UtilisateurService:
    def __init__(self):
        self.repository = UtilisateurRepository()

    def create_utilisateur(self, data):
        return self.repository.create_utilisateur(data)
    
    def list_utilisateurs(self):
        return self.repository.list_utilisateurs
    
    def get_utilisateurs(self):
        return self.repository.get_utilisateurs()

    def get_utilisateur(self, id):
        return self.repository.get_utilisateur(id)

    def update_utilisateur(self, id, data):
        return self.repository.update_utilisateur(id, data)

    def delete_utilisateur(self, id):
        return self.repository.delete_utilisateur(id)
    
class ConsommateurService:
    def __init__(self):
        self.repository = ConsommateurRepository()

    def create_consommateur(self, data):
        return self.repository.create_consommateur(data)
    
    def get_consommateur_by_nom(self, nom: str):
        return self.repository.get_by_nom(nom)


    def get_all_consommateurs(self):
        return self.repository.list_consommateurs()

    def list_consommateurs(self):
        return self.repository.list_consommateurs()


    def get_consommateur(self, id):
        return self.repository.get_consommateur_by_id(id)

    def update_consommateur(self, id, data):
        return self.repository.update_consommateur(id, data)

    def delete_consommateur(self, id):
        return self.repository.delete_consommateur(id)
    
class NuritureService:
    def __init__(self):
        self.repository = NuritureRepository()

    def create_nuriture(self, data, file=None):
        return self.repository.create_nuriture(data, file=file)
    
    def get_nuriture_by_nom(self, nom: str):
        return self.repository.get_by_nom(nom)


    def liste_nuritures(self):
        return self.repository.list_nuritures()

    def get_nuriture(self, id):
        return self.repository.get_nuriture_by_id(id)

    def update_nuriture(self, id, data):
        return self.repository.update_nuriture(id, data)

    def delete_nuriture(self, id):
        return self.repository.delete_nuriture(id)
    
class IngredientService:
    def __init__(self):
        self.repository = IngredientRepository()

    def get_ingredient_by_nom(self, nom):
        return self.repository.get_by_nom(nom)

    def create_ingredient(self, data):
        return self.repository.create_ingredient(data)
    

    def list_ingredient(self):
        return self.repository.list_ingredients()

    def get_ingredient(self, id):
        return self.repository.get_ingredient_by_id(id)

    def update_ingredient(self, id, data):
        return self.repository.update_ingredient(id, data)

    def delete_ingredient(self, id):
        return self.repository.delete_ingredient(id)
    
class CategorieService:
    def __init__(self):
        from app.repositories import CategorieRepository
        self.repository = CategorieRepository()
        
    def get_categorie_by_nom(self, nom):
        return self.repository.get_by_nom(nom)

    def create_categorie(self, data):
        return self.repository.create_categorie(data)

    def liste_categorie(self):
        return self.repository.list_categories()

    def get_categorie(self, id):
        return self.repository.get_categorie_by_id(id)

    def update_categorie(self, id, data):
        return self.repository.update_categorie(id, data)

    def delete_categorie(self, id):
        return self.repository.delete_categorie(id)



class NuritureCategorieService:
    def __init__(self):
        self.repository = NuritureCategorieRepository()

    def create_nuriture_categorie(self, data):
        return self.repository.create_nuriture_categorie(data)

    def get_nuriture_categories(self):
        return self.repository.get_nuriture_categories()

    def get_nuriture_categorie(self, id):
        return self.repository.get_nuriture_categorie(id)

    def update_nuriture_categorie(self, id, data):
        return self.repository.update_nuriture_categorie(id, data)

    def delete_nuriture_categorie(self, id):
        return self.repository.delete_nuriture_categorie(id)




class HistoriqueConsommationService:
    def __init__(self):
        self.repository = HistoriqueConsommationRepository()

    def creer_historique(self, data):
        return self.repository.create_historique(data)

    def verifier_allergie_probable(self, consommateur_id, nuriture_id):
        return self.repository.detecter_allergie_probable(consommateur_id, nuriture_id)





load_dotenv()

class ChatbotService:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "meta-llama/llama-3-8b-instruct"  # modèle IA gratuit

    def poser_question(self, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        system_message = (
            "Tu es un expert en nutrition. Réponds uniquement aux questions sur la nutrition, "
            "la santé alimentaire, les vitamines, les régimes. Sinon, dis que tu ne peux pas répondre."
        )

        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": question}
            ]
        }

        try:
            response = requests.post(self.base_url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

            # Ajoute ce print pour debug
            print("Réponse OpenRouter:", data)

            return data["choices"][0]["message"]["content"]
        except Exception as e:
            print("Erreur API OpenRouter:", str(e))  # log utile
            return f"Erreur OpenRouter : {str(e)}"

    # openrouter.comment include une api avec openrouter pour project flask



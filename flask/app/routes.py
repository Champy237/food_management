from flask import Blueprint, request, jsonify, abort

from app.services import (
    UtilisateurService,
    ConsommateurService,
    NuritureService,
    IngredientService,
    CategorieService,
    NuritureCategorieService,
    HistoriqueConsommationRepository,
    ChatbotService,
)

bp = Blueprint('api', __name__, url_prefix='/api')

utilisateur_service = UtilisateurService()
consommateur_service = ConsommateurService()
nuriture_service = NuritureService()
ingredient_service = IngredientService()
categorie_service = CategorieService()
nuriture_categorie_service = NuritureCategorieService()
historique_service = HistoriqueConsommationRepository()
chatbot_service = ChatbotService()

# --- Routes Utilisateur ---
@bp.route('/utilisateurs', methods=['GET'])
def get_utilisateurs():
    utilisateurs = utilisateur_service.get_utilisateurs()
    return jsonify([u.to_dict() for u in utilisateurs])

@bp.route('/utilisateurs/<int:id>', methods=['GET'])
def get_utilisateur(id):
    utilisateur = utilisateur_service.get_utilisateur(id)
    if not utilisateur:
        abort(404)
    return jsonify(utilisateur.to_dict())

@bp.route('/utilisateurs', methods=['POST'])
def create_utilisateur():
    data = request.json
    utilisateur = utilisateur_service.create_utilisateur(data)
    return jsonify(utilisateur.to_dict()), 201

@bp.route('/utilisateurs/<int:id>', methods=['PUT'])
def update_utilisateur(id):
    data = request.json
    utilisateur = utilisateur_service.update_utilisateur(id, data)
    if not utilisateur:
        abort(404)
    return jsonify(utilisateur.to_dict())


@bp.route('/utilisateurs/<int:id>', methods=['DELETE'])
def delete_utilisateur(id):
    success = utilisateur_service.delete_utilisateur(id)
    if not success:
        abort(404)
    return '', 204

# --- Routes Consommateur ---

@bp.route('/populate_ingredients', methods=['POST'])
def populate_ingredients():
    ingredients_data = [
        {"nom": "Riz", "description": "Riz basmati parfumé."},
        {"nom": "Poulet", "description": "Poulet désossé."},
        {"nom": "Épices", "description": "Mélange d'épices pakistanaises."},
        {"nom": "Viande hachée", "description": "Bœuf haché."},
        {"nom": "Pommes de terre", "description": "Pommes de terre fraîches."},
    ]

    added = []
    for data in ingredients_data:
        if not ingredient_service.get_ingredient_by_nom(data['nom']):
            ingredient = ingredient_service.create_ingredient(data)
            added.append(ingredient.to_dict())

    return jsonify({
        "message": f"{len(added)} ingrédients ajoutés.",
        "ingredients": added
    }), 201

@bp.route('/consommateurs', methods=['GET'])
def create_consommateurs():
    consommateurs = consommateur_service.create_consommateur()
    return jsonify([c.to_dict() for c in consommateurs])

@bp.route('/consommateurs/<int:id>', methods=['GET'])
def get_consommateur(id):
    consommateur = consommateur_service.get_consommateur(id)
    if not consommateur:
        abort(404)
    return jsonify(consommateur.to_dict())

@bp.route('/liste_consommateurs', methods=['GET'])
def get_consommateurs():
    consommateurs = consommateur_service.get_all_consommateurs()
    result = [
        {
            "id": c.id,
            "nom": c.nom,
            "email": c.email
        } for c in consommateurs
    ]
    return jsonify(result), 200

@bp.route('/consommateurs', methods=['POST'])
def create_consommateur():
    data = request.json
    consommateur = consommateur_service.create_consommateur(data)
    return jsonify(consommateur.to_dict()), 201

@bp.route('/consommateurs/<int:id>', methods=['PUT'])
def update_consommateur(id):
    data = request.json
    consommateur = consommateur_service.update_consommateur(id, data)
    if not consommateur:
        abort(404)
    return jsonify(consommateur.to_dict())

@bp.route('/consommateurs/<int:id>', methods=['DELETE'])
def delete_consommateur(id):
    success = consommateur_service.delete_consommateur(id)
    if not success:
        abort(404)
    return '', 204

# --- Routes Nuriture ---


@bp.route('/nuritures', methods=['GET'])
def get_nuritures():
    nuritures = nuriture_service.get_nuritures()
    return jsonify([n.to_dict() for n in nuritures])

@bp.route('/nuritures/<int:id>', methods=['GET'])
def get_nuriture(id):
    nuriture = nuriture_service.get_nuriture(id)
    if not nuriture:
        abort(404)
    return jsonify(nuriture.to_dict())

@bp.route('/liste_nuritures', methods = ['GET'])
def list_nuritures():
    nuritures = nuriture_service.liste_nuritures()
    result = [
        {
            "id": c.id,
            "nom": c.nom,
            "description": c.description,
            "type": c.type,
            "prix": c.prix,
            "image_url": c.image_url,
        } for c in nuritures
    ]
    return jsonify(result),200

@bp.route('/nuritures', methods=['POST'])
def create_nuriture():
    # Pour récupérer les données en formulaire (form fields)
    data = request.form.to_dict()
    image_file = request.files.get('image')
    nuriture = nuriture_service.create_nuriture(data, file=image_file)
    return jsonify(nuriture.to_dict()), 201

@bp.route('/nuritures/<int:id>', methods=['PUT'])
def update_nuriture(id):
    data = request.json
    nuriture = nuriture_service.update_nuriture(id, data)
    if not nuriture:
        abort(404)
    return jsonify(nuriture.to_dict())

@bp.route('/nuritures/<int:id>', methods=['DELETE'])
def delete_nuriture(id):
    success = nuriture_service.delete_nuriture(id)
    if not success:
        abort(404)
    return '', 204

# --- Routes Ingredient ---
@bp.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = ingredient_service.get_ingredients()
    return jsonify([i.to_dict() for i in ingredients])
    
    

@bp.route('/ingredients/<int:id>', methods=['GET'])
def get_ingredient(id):
    ingredient = ingredient_service.get_ingredient(id)
    if not ingredient:
        abort(404)
    return jsonify(ingredient.to_dict())

@bp.route('/ingredients', methods=['POST'])
def create_ingredient():
    data = request.json
    ingredient = ingredient_service.create_ingredient(data)
    return jsonify(ingredient.to_dict()), 201

@bp.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.json
    ingredient = ingredient_service.update_ingredient(id, data)
    if not ingredient:
        abort(404)
    return jsonify(ingredient.to_dict())

@bp.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
    success = ingredient_service.delete_ingredient(id)
    if not success:
        abort(404)
    return '', 204




# --- Routes Categorie ---
@bp.route('/categories', methods=['GET'])
def get_categories():
    categories = categorie_service.get_categories()
    return jsonify([c.to_dict() for c in categories])

@bp.route('/categories/<int:id>', methods=['GET'])
def get_categorie(id):
    categorie = categorie_service.get_categorie(id)
    if not categorie:
        abort(404)
    return jsonify(categorie.to_dict())

@bp.route('/categories', methods=['POST'])
def create_categorie():
    data = request.json
    categorie = categorie_service.create_categorie(data)
    return jsonify(categorie.to_dict()), 201

@bp.route('/categories/<int:id>', methods=['PUT'])
def update_categorie(id):
    data = request.json
    categorie = categorie_service.update_categorie(id, data)
    if not categorie:
        abort(404)
    return jsonify(categorie.to_dict())

@bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_categorie(id):
    success = categorie_service.delete_categorie(id)
    if not success:
        abort(404)
    return '', 204

# --- Routes NuritureCategorie (association many-to-many) ---
@bp.route('/nuriture_categorie', methods=['POST'])
def add_nuriture_to_categorie():
    data = request.json
    nuriture_id = data.get('nuriture_id')
    categorie_id = data.get('categorie_id')
    if not nuriture_id or not categorie_id:
        return jsonify({"error": "nuriture_id and categorie_id required"}), 400
    result = nuriture_categorie_service.repository.update_nuriture_categorie(nuriture_id, categorie_id)
    if not result:
        return jsonify({"error": "Nuriture or Categorie not found"}), 404
    return jsonify({"message": "Nuriture added to categorie"}), 201

@bp.route('/nuriture_categorie', methods=['DELETE'])
def remove_nuriture_from_categorie():
    data = request.json
    nuriture_id = data.get('nuriture_id')
    categorie_id = data.get('categorie_id')
    if not nuriture_id or not categorie_id:
        return jsonify({"error": "nuriture_id and categorie_id required"}), 400
    result = nuriture_categorie_service.repository.remove_nuriture_from_categorie(nuriture_id, categorie_id)
    if not result:
        return jsonify({"error": "Nuriture or Categorie not found or relation doesn't exist"}), 404
    return jsonify({"message": "Nuriture removed from categorie"}), 200


# --- Routes Historique de Consommation ---

@bp.route("historique/",methods=["POST"])
def creer_historique():
    data = request.get_json()
    try:
        historique = historique_service.creer_historique(data)
        return jsonify({
            "id": historique.id,
            "consommateur_id": historique.consommateur_id,
            "nuriture_id": historique.nuriture_id,
            "date_consommation": str(historique.date_consommation),
            "a_eu_malaise": historique.a_eu_malaise
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/historique/allergie", methods=["GET"])
def verifier_allergie():
    consommateur_id = request.args.get("consommateur_id", type=int)
    nuriture_id = request.args.get("nuriture_id", type=int)
    
    if consommateur_id is None or nuriture_id is None:
        return jsonify({"error": "Paramètres requis : consommateur_id et nuriture_id"}), 400

    try:
        allergie_probable = historique_service.verifier_allergie_probable(consommateur_id, nuriture_id)
        return jsonify({"allergie_probable": allergie_probable}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@bp.route("/chatbot", methods=["POST"])
def interroger_chatbot():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Le champ 'question' est requis"}), 400

    reponse = chatbot_service.poser_question(question)
    
    # Vérifie si une réponse est renvoyée
    if not reponse:
        return jsonify({"error": "Aucune réponse générée par le chatbot."}), 500

    return jsonify({"réponse": reponse})







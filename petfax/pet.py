from flask import ( Blueprint, render_template, request )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('index.html', pets = pets)
    
@bp.route('/<int:id>')
def show_pet(id):
    selected_pet = {}
    for pet in pets:
        if pet['pet_id'] == id:
            selected_pet = pet

    return render_template('pet.html', pet = selected_pet)
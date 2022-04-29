import requests
import json

#Pokemon class storing details
class Pokemon: 
    def __init__(self, id, weight, height, abilities, species, types):
        self.id = id 
        self.weight = weight
        self.height = height
        self.abilities = abilities
        self.species = species
        self.types = types

def pokemon(pinput):
    pokemonName = pinput.lower() #Get input to be the same, lowercase, how it will be inputted to the website
    re = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
    coll = json.loads(re.content)
    
    weight = coll["weight"]
    height = coll["height"]
    abilities = coll["stats"][0]["base_stat"]
    species = coll["stats"][1]["base_stat"]
    types = coll["stats"][2]["base_stat"]
    
    pokemond = Pokemon(weight, height, abilities, species, types)
    return pokemond
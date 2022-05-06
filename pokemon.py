import requests
import json

# Pokemon class storing details
class Pokemon: 
    def __init__(self, pinput):
        
        # Get input to be the same, lowercase, how it will be inputted to the website
        pokemonName = pinput 
        re = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
        
        coll = json.loads(re.content)
        self.weight = coll["weight"]
        self.height = coll["height"]
        self.abilities = coll["abilities"]
        self.types = coll["types"]

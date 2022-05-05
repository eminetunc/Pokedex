import requests
import json

#Pokemon class storing details
class Pokemon: 
    def __init__(self, weight, height, abilities, types):
        #self.id = id 
        self.weight = weight
        self.height = height
        self.abilities = abilities
        self.types = types
    

def pokemon(pinput):
    pokemonName = pinput #Get input to be the same, lowercase, how it will be inputted to the website
    re = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
    #print(re.content)
    
    coll = json.loads(re.content)
    weight = coll["weight"]
    height = coll["height"]
    abilities = coll["abilities"]
    types = coll["types"]
    print(abilities)
        
    pokemond = Pokemon(weight, height, abilities, types)
    return pokemond
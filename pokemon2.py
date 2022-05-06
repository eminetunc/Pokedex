import requests
import json

pokemonNum = requests.get("https://pokeapi.co/api/v2/pokemon-species")
pokemonNumStr = str(pokemonNum.json()['count']) 

pokemonName = requests.get("https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit="+pokemonNumStr) #limiting to get all names based on the number of names there are
pokemonNameRes = pokemonName.json()

pokemonNameList = []
for name in pokemonNameRes["results"]:
    pokemonNameList.append(name["name"])

#Pokemon class storing details
class Pokemon: 
    def __init__(self, id, weight, height, abilities, species, types):
        self.id = id 
        self.weight = weight
        self.height = height
        self.abilities = abilities
        self.species = species
        self.types = types
        
'''
def nameId(uInput):
    request = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(uInput)+"/")
    json = request.json()
'''
    
class PokeapiClient:
    def __init__(self, api_base):
        self.api_base = api_base

    def getData(self, species):
        return requests.get(self.api_base + '/pokemon_species/' + str(species) + '/').json()
    
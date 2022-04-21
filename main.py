import requests
import json

pokemonNum= requests.get("https://pokeapi.co/api/v2/pokemon-species")
pokemonNumStr= str(pokemonNum.json()['count']) 

pokemonName= requests.get("https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=") #limiting to get all names 0-20
pokemonNameRes= pokemonName.json()

pokemonNameList= []
for name in pokemonNameRes["results"]:
    pokemonNameList.append(name["name"])

#Pokemon Class
class Pokemon: 
    def __init__(poke, id, name, height, abilities, species, types):
        poke.id = id 
        #poke.id = requests.get("https://pokeapi.co/api/v2/pokemon/")
        poke.name = name
        poke.height = height
        poke.abilities = abilities
        poke.species = species
        poke.types = types
    
#class Pokedex:
#    def __init__():
        
def nameId(uInput):
    request=requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(uInput)+"/")
    json=request.json()

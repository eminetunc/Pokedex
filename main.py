import requests
import json
from tkinter import *

pokemonNum = requests.get("https://pokeapi.co/api/v2/pokemon-species")
pokemonNumStr = str(pokemonNum.json()['count']) 

pokemonName = requests.get("https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit="+pokemonNumStr) #limiting to get all names based on the number of names there are
pokemonNameRes = pokemonName.json()

pokemonNameList = []
for name in pokemonNameRes["results"]:
    pokemonNameList.append(name["name"])

#Implementing UI
root = Tk()
root.title("Pokedex")

label = Label(root, text = "Enter the name of your pokemon: ", fg="red")
label.pack()

input = Entry(root)
input.pack()

def search():
    display.delete("1", END) #Will delete anything entered in the box that will display the output
    pokemon= input.get()
    try:
        pass
    except AttributeError:
        display.insert(END, "Please enter a pokemon.")
    
button = Button(root, text="Submit", fg="red", bg="yellow")
button.pack()

display= Text(root)
display.pack()

root.mainloop()

#Pokemon class storing details
class Pokemon: 
    def __init__(self, id, name, weight, height, abilities, species, types, defense):
        self.id = id 
        self.name = name
        self.weight = weight
        self.height = height
        self.abilities = abilities
        self.species = species
        self.types = types
        self.defense = defense
        
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

# sample usage:
#pokedex = PokeapiClient('https://pokeapi.co/api/v2')
#print(pokedex.getData('pikachu'))
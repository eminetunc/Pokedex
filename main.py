import requests
import json
from tkinter import *
import pokemon2
#import pokebase as pb

#Implementing UI
#UI display
root = Tk()
root.title("Pokedex")
root.geometry("600x700")
label = Label(root, text = "Enter the name of your pokemon: ", fg="red", pady=20)
label.pack()

#getting 
def printValue():
    pname = input.get()
    
input = Entry(root)
input.pack()

def search():
    display.delete("1.0", END) #Will delete anything entered in the box that will display the output
    #pokemon= PokeapiClient.getData(input.get())
    pokemon = pokemon.pokemon(printValue)
    try:
        response = requests.get(pokemon.sprites.front_default)
        abilities = " "
        types = " "
        for ability in pokemon.abilities: 
            abilities += ability.ability.name
        for poketype in pokemon.types: 
            types += poketype.type.name
        info = f"""{input.get().capitalize()}
        Abilities: {pokemon.abilities}
        Height: {pokemon.height}
        ID: {pokemon.id}
        Species: {pokemon.species}
        Types: {pokemon.types}
        Weight: {pokemon.weight}
        """
        display.insert(END, info)
          
    except AttributeError:
        display.insert(END, "Please enter a pokemon.")
    
button = Button(root, text="Submit", fg="red", bg="yellow", command=search)
button.pack()

display= Text(root)
display.pack()

root.mainloop()

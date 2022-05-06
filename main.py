import pokemon
from tkinter import *

# UI display
root = Tk()
root.title("Pokedex")
root.geometry("700x700")
label = Label(root, text = "Enter the name of your pokemon: ", fg = "red", pady = 20)
label.pack()

# Getting input
def printValue():
    return input.get()
    
input = Entry(root)
input.pack()

def search():
    # Will delete anything entered in the box that will display the output
    display.delete("1.0", END)
    pokemon_object = pokemon.Pokemon(printValue())
    
    abilities = " "
    types = " "
    
    for ability in pokemon_object.abilities: 
        abilities += ability["ability"]["name"]
    
    for poketype in pokemon_object.types: 
        types += poketype["type"]["name"]
        
    info = f"""{input.get().capitalize()}
    Abilities: {ability["ability"]["name"]}
    Height: {pokemon_object.height}
    Types: {poketype["type"]["name"]}
    Weight: {pokemon_object.weight}
    """
    display.insert(END, info)
    
button = Button(root, text = "Submit", fg = "red", command = search)
button.pack()

display = Text(root)
display.pack()

root.mainloop()

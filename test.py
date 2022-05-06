import pokemon

def test_type():
    # Given
    pokemon_name = "pikachu"
    expected_type = "electric"
    p_pokemon = pokemon.Pokemon(pokemon_name)
    
    # When
    types = " "
    for poketype in p_pokemon.types: 
        types += poketype["type"]["name"]
    actual_type = poketype["type"]["name"] 
    
    # Then 
    assert expected_type == actual_type

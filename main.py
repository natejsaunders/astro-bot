from wikidata.client import Client

client = Client()

planet_ids = {
    'earth': 'Q2',
    'saturn': 'Q193'
}

property_ids = {
     'flattening': 'P1102',
     'population': 'P1082',
     'location': 'P276',
     'periapsis': 'P2244',
     'albedo': 'P4501',
     'density': 'P2054',
     'temperature': 'P2076',
     'area': 'P2046'
}

print("Hello there!")
print("I am ASTROBOT, please ask me any questions you have about our solar system...")

quit = False
while not quit:
    user_input = input("> ").lower().strip()

    words_input = user_input.split(' ')

    # Only processes "what is the {property} of earth" currently

    if words_input[0] == 'exit':
         quit = True
         break
    elif words_input[0] == 'what':
        if words_input[1] == 'is':
            if words_input[2] == 'the':
                # Check property

                input_property = words_input[3]
                planet = words_input[5]

                planet_id = planet_ids[planet]
                property_id = property_ids[input_property]

                planet_entity = client.get(planet_id, load=True)
                property_entity = client.get(property_id)

                planet_data = planet_entity.getlist(property_entity)
                for value in planet_data:
                    print(value)

    else:
        print("I do not understand your question.")

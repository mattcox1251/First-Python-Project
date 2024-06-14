# list of different destinations
destinations = ["Paris, France", "Shanghai, China"
                , "Los Angeles, USA", "Sao Paulo, Brazil",
                "Cairo, Egypt"]
# our traveler
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

#function that takes in the destination and returns the index in the list
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#function that returns the index of the travelers destination in the list
def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# empty list that creates attractions for each destination in the destantions list above
attractions = [[] for destination in destinations]
print(attractions)

# function that adds on attraction to the empty list
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
print(attractions)



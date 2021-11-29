import json

def building_with_id(_, info, _id):
    with open('./data/buildings.json') as file:
        data = json.load(file)
        for building in data['buildings']:
            if building['id'] == _id:
                return building

def resolve_residents_in_building(building, info):
    print(building)
    with open('./data/residents.json') as file:
        data = json.load(file)
        residents = [
            resident 
            for resident 
            in data['residents'] 
            if resident['building'] 
            == building['id']]
        return residents


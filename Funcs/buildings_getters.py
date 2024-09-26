import json

def get_buildings():
    with open("./Data/buildings.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"buildings": data}

if __name__ == "__main__":
    print(get_buildings())
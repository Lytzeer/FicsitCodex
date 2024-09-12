import json

def get_buildings():
    with open("./Data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"buildings": data["buildings"]}

if __name__ == "__main__":
    print(get_buildings())
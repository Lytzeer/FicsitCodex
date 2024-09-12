import json

def get_schematics():
    with open("./Data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"schematics": data["schematics"]}

if __name__ == "__main__":
    print(get_schematics())
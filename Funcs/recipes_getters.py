import json

def get_recipes():
    with open("./Data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"recipes": data["recipes"]}

if __name__ == "__main__":
    print(get_recipes())
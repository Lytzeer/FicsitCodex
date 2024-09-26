import json

def get_recipes():
    with open("./Data/recipes.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"recipes": data}

if __name__ == "__main__":
    print(get_recipes())
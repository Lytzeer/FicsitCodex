import json

def get_items():
    with open("./Data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"items": data["items"]}

if __name__ == "__main__":
    print(get_items())
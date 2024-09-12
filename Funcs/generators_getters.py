import json

def get_generators():
    with open("./Data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"generators": data["generators"]}

if __name__ == "__main__":
    print(get_generators())
import json

def get_generators():
    with open("./Data/generators.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"generators": data}

if __name__ == "__main__":
    print(get_generators())
import json

def get_miners():
    with open("./Data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"miners": data["miners"]}

if __name__ == "__main__":
    print(get_miners())
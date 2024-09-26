import json

def get_items():
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"items": data}

def get_item_by_id(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"item": data[item_id]}


def get_item_name(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['name']

def get_item_description(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['description']

def get_item_stack_size(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['stackSize']

def get_item_sink_points(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['sinkPoints']

def get_item_energy_value(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['energyValue']

def get_item_radioactive_decay(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['radioactiveDecay']

def get_item_liquid(item_id):
    with open("./Data/items.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[item_id]['liquid']

def get_item_all_primary_info(item_id):
    name = get_item_name(item_id)
    desc = get_item_description(item_id)
    stack = get_item_stack_size(item_id)
    sink = get_item_sink_points(item_id)
    energy = get_item_energy_value(item_id)
    radioactive = get_item_radioactive_decay(item_id)
    liquid = get_item_liquid(item_id)
    return {"name": name, "description": desc, "stackSize": stack, "sinkPoints": sink, "energyValue": energy, "radioactiveDecay": radioactive, "liquid": liquid}
    

if __name__ == "__main__":
    print(get_item_all_primary_info("49"))
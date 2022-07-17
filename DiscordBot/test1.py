import json


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


msgs = {
    "clear": [1, 2]
}

write(msgs, 'jclear.json')

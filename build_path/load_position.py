import json

def load_data():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    data = load_data()
    print(data)
    print(type(data))
    max_page_count = 0
    for dist in data.keys():
        for pos in data[dist].keys():
            max_page_count = max(max_page_count, data[dist][pos]["page_count"])
    print(max_page_count)

from collections import OrderedDict
import json

with open('allTopping.json', encoding="utf-8") as json_file:
    allTopping = json.load(json_file)

with open('mr.json', encoding="utf-8") as json_files:
    mrTopping = json.load(json_files)

print(type(mrTopping))
print(mrTopping[0])

allTopping = []

for topping in mrTopping:
    lastList = []
    toppingList = topping['topping'].split(',')
    for i in toppingList:
        lastTopping = i.strip()
        lastList.append(lastTopping)
        if lastTopping in allTopping:
            print("이게 포함되네 4")
        else:
            allTopping.append(lastTopping)

    topping["topping"] = lastList

with open('mrTopping.json', 'w', encoding="utf-8") as make_files:
    json.dump(allTopping, make_files, ensure_ascii=False, indent="\t")

with open('mr.json', 'w', encoding="utf-8") as make_files:
    json.dump(mrTopping, make_files, ensure_ascii=False, indent="\t")


file_data = OrderedDict()



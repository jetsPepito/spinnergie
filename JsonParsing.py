import json
import re
import shutil

def modifyJson_(js, tab, val):
    js.seek(0)
    data = json.load(js)
    modifyJson(js, tab, val, data)
    js.seek(0)
    json.dump(data, js, indent=4)
    js.truncate()


def modifyJson(js, tab, val, data):
    if len(tab) == 1:
        data[tab[0]] = val
        return
    data2 = data[tab[0]]
    tab.pop(0)
    modifyJson(js, tab, val, data2)


def parsing(jsonFile, changingFile):
    with open(changingFile, "r") as changes:
        shutil.copy2(jsonFile, "newJson.json")
        with open("newJson.json", "r+") as js:
            lines = changes.readlines()
            for l in lines:
                tab = []
                parsedline = re.search('(.*): (.*)', str(l))
                val = parsedline.group(2)
                id = parsedline.group(1)[1:-1]  #strip first and last double quote
                tab = id.split(".")
                print(val)
                print(id)
                modifyJson_(js, tab, val)
        js.close()
    changes.close()


if __name__ == '__main__':
    parsing("test.json", "changes")
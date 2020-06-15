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
        if "[" in tab[0]:
            pars = re.search('(.*)\[(.*)\]', tab[0])
            v = pars.group(2)
            data[pars.group(1)][int(v) - 1] = val
        else:
            data[tab[0]] = val
        return

    if "[" in tab[0]:
        pars = re.search('(.*)\[(.*)\](.*)', tab[0])
        v = pars.group(2)
        newData = data[pars.group(1)][int(v) - 1]
    else:
        newData = data[tab[0]]
    tab.pop(0)
    modifyJson(js, tab, val, newData)


def main(jsonFile, changingFile):
    with open(changingFile, "r") as changes:
        shutil.copy2(jsonFile, "newJson.json")
        with open("newJson.json", "r+") as js:
            lines = changes.readlines()
            for l in lines:
                parsedline = re.search('"(.*?)": (.*)', str(l))
                val = parsedline.group(2)
                id = parsedline.group(1)
                tab = id.split(".")
                modifyJson_(js, tab, json.loads(val))
        #Closing files
        js.close()
    changes.close()


if __name__ == '__main__':
    main("test.json", "changes")

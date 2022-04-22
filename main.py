import json, secrets
from time import sleep

try:
    with open("kanji.json") as file:
        list_of_kanji = json.loads(file.read())
except:
    pass
    #to continue
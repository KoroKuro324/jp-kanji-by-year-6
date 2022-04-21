import json, secrets
from time import sleep

with open("kanji.json", encoding="UTF-8") as fl:
    kanji = json.loads(fl.read())

def quiz(school: str, grade: str):
    correct = []
    for x in range(10):
        choosen_kanji = secrets.choice(kanji[school][grade])
        print(f" Word is:\n {choosen_kanji['kanji']}")
        text = input("> ")
        if text == choosen_kanji["onyomi"] or text == choosen_kanji["pronunciation"]:
            correct.append(text)
            print(" Correct!\n")
            sleep(1)
        else:
            print(" Wrong!")
            print(f" The correct one is:\n {choosen_kanji['onyomi']} or {choosen_kanji['pronunciation']}\n")
            sleep(1)
    if len(correct) == 0:
        print(f" You scored {len(correct)}/10...")
    elif len(correct) < 5:
        print(" Better luck next time!")
        sleep(2)
    else:
        print(f" You scored {len(correct)}/10")
    print("\n\n")

while 1:
    print(" 1. 教育漢字 [primary school]\n 2. Soon")
    school = input("> ")
    if school == "教育漢字" or school == "primary school" or school == "教育漢字" or school == "1":
        print(" 1. 一年生 [first grade]\n 2. 二年生 [second grade]\n 3. 三年生 [third grade]")
        grade = input("> ")
        if grade == "1":
            quiz(school="教育漢字", grade="一年生")
        elif grade == "2":
            pass
        elif grade == "3":
            pass
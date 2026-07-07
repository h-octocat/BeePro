import os
import re

import requests
from dotenv import load_dotenv
from gtts import gTTS
from playsound import playsound
from unidecode import unidecode


def initEnvironment():
    load_dotenv()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("tput clear")


def getDictionaryLink(formattedWord):
    return f"https://dictionaryapi.com/api/v3/references/collegiate/json/{formattedWord}?key={os.environ['DICT_API']}"


def readText(text):
    if text == "" or text == " ":
        return
    tts = gTTS(text, lang="en")
    tts.save("output.mp3")
    playsound("output.mp3")
    os.system("rm -rf output.mp3")


def spellOut(word):
    for letter in word:
        readText(unidecode(letter))


def getDict(word):
    word = clean(word)
    defword = word
    if "OR" in word:
        defword = word.split(" OR ")[0]
    defjson = requests.get(getDictionaryLink(defword)).json()
    if defjson and type(defjson[0]) is dict:
        definition = defjson[0]["shortdef"][0]
    else:
        definition = "definition error"

    return definition


def clean(text):
    return unidecode(re.sub(r"[^a-zA-Z]", "", text).lower())

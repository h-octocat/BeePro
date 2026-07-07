import time

from helper import clean, clear, getDict, initEnvironment, readText, spellOut

initEnvironment()
correct = 0
clear()
file = input(
    "Welcome to study! Make sure not to type anything unless prompted to spell it! What file are you studying from: "
)
text = ""
with open(f"{file}", "r+") as f:
    text = f.read()

words = text.split("\n")
for word in words:
    if word == "":
        continue

    readText(word)
    spellOut(word)
    readText(word)
    print(f"Again, it's spelled {word}")
    definition = getDict(word)
    if definition == "definition error":
        print("Invalid word or definition processing error!")
    else:
        print(f"It means {definition}")
    time.sleep(4)
    clear()
    time.sleep(1)
    userInput = input("Now spell it! ")
    if clean(userInput) != clean(word):
        print(f"Incorrect. Its spelled {word}.")
    else:
        correct += 1

print(f"You got {correct / len(words) * 100}% percent correct!")

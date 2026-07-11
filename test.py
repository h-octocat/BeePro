from helper import clean, clear, getDict, initEnvironment, readText

initEnvironment()
clear()
file = input("Welcome to spelling marathon! What file to read from?")
text = ""
with open(f"{file}", "r+") as f:
    text = f.read()

words = text.split("\n")
# number of words
no_words = len(words)
wrong_words = []
amount_correct = 0

print(
    "The word will be read to you. Try and spell it (all lowercase except for proper nouns)!"
)
response = ""
for word in words[:]:
    if word == "":
        no_words -= 1
        continue
    while True:
        readText(word)
        definition = getDict(word)
        response = input(
            "How do you spell that? Type repeat to repeat it, stats for how many words are left, and def for the definition of the word. "
        )
        if (
            response != "repeat"
            and response != "stats"
            and response != "save"
            and response != "def"
        ):
            break
        if response == "stats":
            words_left = len(words) - (words.index(word) + 1)
            print(f"You have {words_left + 1} words left")
        elif response == "def":
            if definition == "definition error":
                print("Invalid word or definition processing error!")
            else:
                print(f"It means {definition}")

    if clean(response) == clean(word):
        amount_correct += 1
        print("Nice! You got it correct!")
        continue
    else:
        if "OR" in word:
            correct = False
            word_components = word.split(" OR ")
            for word_component in word_components:
                if clean(response) == clean(word_component):
                    amount_correct += 1
                    print("Nice! You got it correct!")
                    correct = True
                    break
            if correct:
                continue
        print(f"Better luck next time! The correct spelling was: {clean(word)}")
        wrong_words.append(word)

percent_correct = (amount_correct / no_words) * 100

print(f"You got {percent_correct}% correct!")

if percent_correct != 100:
    saveyesno = input(
        "Would you like to save the questions you got wrong in a seperate file to test on? (y/n)"
    )

    if saveyesno == "y":
        if "wrong" not in file:
            with open(f"{file.replace('.txt', '')}-wrong.txt", "w+") as f:
                f.write("\n".join(wrong_words))

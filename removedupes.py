file = input("Please provide the file name: ")
contents = ""
with open(file, "r") as f:
    contents = f.read()

unique = list(set(contents.split("\n")))

with open(file, "w") as f:
    f.write("\n".join(unique))

# Replace all repetation of donkey from prob4 file to ###

word = "donkey"

with open("prob4.txt") as f:
    content = f.read()

newcontent = content.replace(word, "###")

with open("prob4.txt", "w") as f:
    f.write(newcontent)
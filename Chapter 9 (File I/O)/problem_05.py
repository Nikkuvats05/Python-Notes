# ONLY one word nhi list me jitne bhi words sbko unki length *# se replace krna h 

words = ["Donkey", "good", "will"]

with open("prob4.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, len(word)*"#")

with open("prob4.txt", "w") as f:
    f.write(content)

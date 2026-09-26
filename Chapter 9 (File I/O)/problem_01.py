# Reas poem.t5xt and tell is word"twinkle" is present in it or not?

f = open("poem.txt")

content = f.read()
if "twinkle" in content:
    print("twinkle is present in content")
else:
    print("twinkle is not present in content")

f.close()
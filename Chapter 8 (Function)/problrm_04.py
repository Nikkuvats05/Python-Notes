# Write a python function to remove a given word from a listad strip it at the same time. hint: Remove all an from given list : l = ["Mohan", "Rohan", "an" , "Shayam"]

def rem(l, word):
    for item in l:
        if(item == word):
            l.remove(word)
            return l
        
l = ["Mohan", "Rohan", "an" , "Shayam"]
rem(l, "an")
print(l)
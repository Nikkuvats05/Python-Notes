# In a message "Nikhil is written in any case tell this name is present or not like NIKHIL , Nikhil, NIKhil, niKHil etc all are accepted as present"
post = input("Enter the post = ")

if("nikhil" in post.lower()):
    print("Its talking about Nikhil")

else:
    print("This post is not about Nikhil")
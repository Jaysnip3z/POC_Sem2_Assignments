text = input("Enter some text: ")

result = text.find("the")

if result == -1:
    print("the word the is not in the string")
else:    
    print("The word is in the string")
    print("The word the is at position: ", result)     

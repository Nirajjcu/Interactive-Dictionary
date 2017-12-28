import json
from difflib import get_close_matches
data = json.load(open("data.json"))
print ("This is the dictionary Brought to you By")
print ("******NIRAJ BUDHATHOKI**********")
play = 'y'
while play == 'y':
    while True:
        xl = input("Type the word to find the meaning: ").lower()
        if xl in data:
            for i in data[xl]:
                print(i)
            break
        elif xl.title() in data:
            for i in data[xl.title()]:
                print(i)
            break
        elif xl.upper() in data:
            for i in data[xl.upper()]:
                print(i)
            break

        elif len(get_close_matches(xl,list(data.keys())))!=0:
            print("Did you mean the following words")
            print (get_close_matches(xl,list(data.keys())))
        else:
            print("Please check the word again ")
    play = ""
    while not (play == 'y' or play == 'n'):
        play = (input("Do you want to search the meaning again(y) or (n): ")).lower()[0]

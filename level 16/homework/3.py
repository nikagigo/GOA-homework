# 3) შეადარეთ თქვენი ასაკი მომხმარებლის შემოტანილ ასაკს, თუ თქვენი ასაკი მეტია 
# მომხმარებლის ასაკზე უთხარით რომ თქვენ მასზე დიდი ხართ, თუ მასზე პატარა ხართ
# დაუპრინტეთ რომ მასზე პატარა ხართ და სხვა შემთხვევაში დაუპრინტეთ რომ ტოლები ხართ.
 
myage = int(17)

age = int(input("enter your age"))

if myage > age:
    print("im older than you")
elif myage < age:
    print("you are older than me")
elif myage == age:
    print("we are same age")
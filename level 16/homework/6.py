# 6) თქვენ დაგპატიჟეს პატარა ბავშვის დაბადების დღეზე გასართობ ცენტრში, თქვენთან ერთად ამ გასართობ ცენტრში დაპატიჟეს 
# 10 ადამიანი და ამ 10 ადამიანიდან ერთ ერთი ნიკოლოზია. ნიკოლოზს უთხრეს რომ მას შეუძლია ბავშებთან ერთად გაერთოს
# თუ ის ფეხსაცმელებს გაიხდის და ქურთუკს საკიდზე ჩამოკიდებს (True და False-ს გამოყენება დაგჭირდებათ). თქვენი მიზანია
# გაარკვიოთ ნიკოლოზმა შეასრულა ეს წესები თუ არა, ანუ შეუძლია თუ არა მას ბავშებთან ერთად გართობა.
ki = "true"
jacket = input("do you have a jacket on?")
shoes = input("do you have a shoes on?")

if jacket == "true" and shoes == "true":
    print("you can play with childrens")
elif jacket == "false" and shoes == "true":
    print("you can't play with childrens")
elif jacket == "true" and shoes == "false":
    print("you can't play with childrens")
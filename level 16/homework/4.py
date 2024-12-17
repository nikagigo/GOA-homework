# 4) გიორგიმ შექმნა ზოოპარკი სადაც შესვლა მხოლოდ კონკრეტული აღნაგობის ხალხს შეუძლიათ. 
# გიორგი ზოოპარკში უშვებს ხალხს რომელიც 180 სანტიმეტრზე მაღლები არიან და 50-90 კილოს 
# შორის არიან წონით. თქვენი მისიაა რომ მომხმარებელს შემოატანინოთ წონა და სიმაღლე და 
# გაარკვიოთ შეუძლია თუ არა მომხმარებელს ზოოპარკის მონახულება.
height = int(input("enter your height"))
weight = int(input("enter your weight"))

if height < 180:
    print("you cant go to zoo")
elif weight < 50 or weight > 90:
    print("you cant go to zoo")
elif height > 180:
    print("you can go to zoo")
elif weight > 50 and weight < 90:
    print("you can go to zoo")
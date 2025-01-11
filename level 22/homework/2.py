# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ რიცხვების საშუალო არითმეტიკული
number = int(input("sheiyvanet ricxvi "))
total_sum = 0
for i in range(1,number + 1):
    total_sum += i
    average = total_sum / number
    print(average)
#  3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის კვადრატის ჯამი
number = int(input("sheiyvanet ricxvi"))
total_sum = 0
for i in range(1,number + 1):
 total_sum += i
 numb1 =  total_sum * number
 print(numb1)
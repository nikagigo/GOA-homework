# 2) გამოიყენეთ or ოპერატორი, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები.
num = int(input("enter number"))
if num >= 10 or num <= 50:
    print("this number is more then 10 and less than 50")
elif num < 10:
    print("number is bellow 10")
elif num > 50:
    print("this number is more than 50")
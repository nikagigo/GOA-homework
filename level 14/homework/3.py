# 3)შეამოწმეთ, არის თუ არა მოცემული ციფრი დადებითი ან ნული, თუმცა არ არის უარყოფითი.
num = int(input("enter number "))

if num < 0:
    print("this number is negative")
elif num > 0:
    print("this number is positive")
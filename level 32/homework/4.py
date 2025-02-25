# 4) გააკეთეთ Find Maximum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მაქსიმუმი ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [546]
num = [1, 546, 456 ,123]
maxnum = num[0]
for i in range(len(num)):
    if i > maxnum:
        maxnum = num[i]
print(maxnum)
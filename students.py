n = int(input("enter the number of students: "))
data = {}
kecheng = ('physics','maths','history')
for i in range(0,n):
    name = input("enter name {}: ".format(i+1))
    score = []
    for x in kecheng:
        score.append(int(input("enter the score of {}".format(x))))
    data[name] = score
for x,y in data.items():
    total = sum(y)
    print("{} 's total marks {}".format(x,total))
    if total < 120:
        print(x,"failed !")
    else:
        print(x,"passed!")



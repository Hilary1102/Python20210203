math=[]
name=[]
total=0
high=0
low=100
n = int(input("How many people in this class?"))


for i in range(n):
    stuname = int(input("Please input the name"))
    score   = int(input("Please input the score"))
    total = total+score
    name.append(stuname)
    math.append(score)
    
for i in range(n):
    score = int(input("Please input the score"))
    total = total+score
    if high < score:
       high = score
    if low  > score:
       low  = score
    math.append(score)
    
for i in range(n):    #比較最高分
    if math[i] > high:
       high = math[i]
       highname = name[i]
       
for i in range(n):   #比較最低分
    if math[i] < low:
        low = math[i]
        lowname = name[i]
    
average = total / n
print(score)
print("average:",average)
print("high",high)
print("low",low)
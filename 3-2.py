math=[]
total=0
high=0
low=100
n = int(input("How many people in this class?"))

for i in range(n):
    score = int(input("Please input the score"))
    total = total+score
    if high < score:
       high = score
    if low  > score:
       low  = score
    math.append(score)

average = total / n  #算平均
print(score)
print("average:",average)
print("high",high)
print("low",low)
   
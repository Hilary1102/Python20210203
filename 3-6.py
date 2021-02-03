math = list()
total = 0
avg = 0

n = input("How many people in the class?")
n = int(n)


for i in range(n):
    name = input("Please input the name:")
    score = input("Please input the score:")
    score = int(score)
    
    operson = list()
    operson.append(name)
    operson.append(score)
    
    math.append(operson)
    
for item in math:
        total = total+item[1]
average = total / n
print("The average is",average)


high = 0
person = ' '
for item in math:
    if item[1]>high:
        high = item[1]
        persom = item[0]
print(person,  "got the highest score", high)


low = 100
person = ' '
for item in math:
    if item[1] < low:
        low = item[1]
        person = item[0]
print(person, "got the lowest score", low)

        
        
        
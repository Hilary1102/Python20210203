math=[]
total=0
high=0
low=100
n= int(input("How many student in this class?")

for i in range(n):
    stuname = input("Please input the name")
    score = int(input("Please input the score"))
    total =total+score
    math.append(stuname)
    math.append(score)
    
for i in range(1,n*2,2):
    if math[i] > high:
        high = math[i]
        highname[i-1]
            
for i in range(1,n*2,2):
    if math[i] < low:
         lowname = math[i-1]
        
        
            
            
    
    
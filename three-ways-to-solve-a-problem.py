#Let's observe 3 solutions to get the sum of natural numbers.

#first formula finding sum of natural numbers

print("Hello, World!")
i = 0

for(x) in range (1, 6):

    
    i += x 
    print(x)



print(i)



#n * (n + 1) // 2
#second formula for finding sum of natural numbers
n = 5


n = n * (n + 1) //2

print(n)

#the second formula is more efficient because
#it gets the sum all in one line
print("-----------------")
#third formula (the top two may be less confusing)
j = 0
k = 0
for (x) in range(1, 6):
    for (y) in range(1, x + 1):
        j += 1
        k += 1
print("Total j: ", j, " and total y: " , k)


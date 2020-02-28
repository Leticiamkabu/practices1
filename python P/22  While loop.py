
#i = 0

#numbers = []

#while i < 6:
    #print ("At the top i is %d" % i)
    #numbers.append(i)


    #i = i + 1
    #print("Numbers now: ",numbers)
    #print("At the bottom i is %d" % i)


#print ("The numbers: ")

#for num in numbers:
    #print (num)





#this is my exercise
def my(set,i,increment):
    while i < set:
        print("At the top i is %d" % i)
        i = i + increment

my(6,0,2)

#now lets see something
def m(set,i,increment):
    numbers = []
    while i < set:
        print("At the top i is %d" %i)
        numbers.append(i)

        i = i + increment
        print("Number now:  ", numbers)
        print("At the bottom i is %d" % i)
        
print("The numbers: ")

for num in numbers:
      print (num)


m(6,0,1)


#lets also see this
i = 0
numbers = []

for i in range(0,6):
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print ("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)
    

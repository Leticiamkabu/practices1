# this is the main function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers! " %boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# we print the statement and call the main function below it with its values
print ("We an just give the function numbers directly:")
cheese_and_crackers(20,30)


#We print the statement an assign values to variables
print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# we call the main function and place the previous variables within its arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# we print the statement and perform maths within the main functions argument section
print ("We can even do the math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# this prints the string 
print("And we can combine the two, variable and math:")
#This also calls the main function and it ontains a variable and a number
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



def me(School,Like):
    print("I attend %s" %School)
    print("What do you like: %s" %Like)



print(" This is me")
me("KTU","Music")


print("This is also included")
Collage = "UCC"
Hate= "GJHG"

me(Collage, Hate)



#This is a string
x = "There are %d types of people." %10
#This is a variable containing a string
binary = "binary "
do_not = "don't"

#This variable contains a string and two other strings
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said : %r" %x)
print ("I also said: '%s'." %y )

#This variable contains a boolean figure
hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"

#This prints both the sting and boolean figure.
print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with  a rigth side."
#This produes a long sentence with the '+' character because it is a concatination character
print (w + e)


#this will print '.' 10 times
print ("." * 10)

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter %("I had this thing.","That you could type up rigth.","But it didn't sing.", "So I said goodnight."))




#this will dislay the months in a horizontal line
months = "Jan\n Feb\n Mar\n Apr"
print(months)

#This will maintain the writing in the way you see it
print("""
Good old days
When love was the most important
And evil was led out of our lives
""")

print("I am 6'2\"tall")
print('I am 6\'2" tall.')


#while True:
    #for i in ['/','-','|','\\','|']:
       # print ('%s\r' % i)


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm Split\non a line."
backslash_cat = "I'm\\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)




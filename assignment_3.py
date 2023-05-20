#################################################
##       EXCERCISE 1 30 MARKS                  ##
#################################################
##                                             ##
## student name:sibuyi cs                      ##
## student no:220590836                        ##
## date:20 may 2023                            ##
## assignment 3:python                         ##
##                                             ##
#################################################


#################################################
###       problem 1 -10 marks points           ##
#################################################

s='fullstackslp'
print(s[0])             #f
print(s[len(s)-1])      #p
print(s[4:9])           #stack
print(s[9:12])          #slp
print(s[7:10])          #cks

reversed_string = s[::-1]
print(reversed_string)


#############################################
##        problem 2-LISTS -5 Marks         ##
#############################################
d1={'simple_key':'hello'}
print(d1['simple_key'])     #hello

d2={'k1':{'k2':'hello'}}
print(d2['k1']['k2'])       #hello

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]} 
print(d3['k1'][0]['nest_key'][1][0]) #hello


#####################################################
##           Problem 4 - 4 Marks                   ##
#####################################################


mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(set(mylist))

###################################################
##              Problem 5 - 5 Marks              ##
###################################################

age=45
name = "Kyle"
# "Hello my dog's name is Kyle and he looks 45 years old"
print("Hello my dog's name is {} and he looks {} years old".format(name, age))



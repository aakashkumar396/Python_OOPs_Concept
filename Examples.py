"""
my_range = range(1,21)
#print(list(my_range))
print([10 * x for x in my_range])



#MAP Function
my_range = range(1,21)
print(list(map(str, my_range)))   #map function syntax=> map(func, iterable)


#Removing Duplicates
a = ["1",1,"1",2]
a = list(set(a))
print(a)



#Dictionary
d = {"a":1,"b":2}
d1 = dict(a=1,b=2)
print(type(d))
print(type(d1))
print(d1["b"])   #printing B key value  syntax=> print(variable_name["key"])

d2 = dict(a=1,b=2,c=3)
print(d2["a"] + d2["b"])  #adding two dictionary key values


#Adding Dictionary Key
d3 = {"a":1,"b":2}
d3["c"]=3    #syntax=> var[key]=value
print(d3)


#Sum of Dictionary values
d3 = {"a":1,"b":2,"c":3}
print("Sum of dictionary values using SUM() : ",sum(d3.values()))

def sum(n):
    sum = 0
    for i in n.values():
        sum += i
    return sum
d4 = {"a":1,"b":2,"c":3}
print("Sum of dictionary values using def funct() : ",sum(d4))


#Dictionary FIltering using Comprehension
#Qouestion Filter the dictionary by removing all items with a value of greater than 1.
d5 = {"a":1,"b":2,"c":3}
#dictionary filtering syntax=> dict((key,value) condition)
d5 = dict((key,value) for key,value in d5.items() if value <=1)
print(d5)
"""
"""
#Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20,
#and 21 to 30, respectively. Then print out the dictionary in a nice format.

from pprint import pprint
d = {"a":list(range(1,11)),"b":list(range(11,21)),"c":list(range(21,31))}
pprint(d)

#Access the third value of key b  from the dictionary.
pprint(d["b"][2])

print(d.items())
for key,value in d.items():
    print(key,"value has ",value)
"""
"""
OUTPUT:-
a value has  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b value has  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c value has  [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
"""

"""
#Create a function that calculates acceleration given initial velocity v1,
#final velocity v2, start time t1, and end time t2. The formula for acceleration is:

def accelaration(v1,v2,t1,t2):
    a = 0
    a = (v2 - v1) / (t2 - t1)  #accelation formula
    return a

acc = accelaration(0,10,0,20)
print("Accelaration value :",acc)
"""

"""
#Please write a function that calculates liquid volume in a sphere using the
#following formula. The radius r  is always 10, so consider making it a default parameter.

def volume(h, r=10):
    liq_vol = 0
    pi = 3.14
    liq_vol = ((4*pi*r**3)/3) - (pi*h**2*(3*r - h)/3)
    return (liq_vol)

liq = volume(2)
print(liq)
"""

"""
c = 1
def foo():
    #gloabal c      if we want to access outside function Global keyword will use
    #c=2
    return c         #Global variable output=3        Local global= 2

c = 3
print(foo())
#print(c)
"""

"""
#Create a function that takes any string as input and
#returns the number of words for that string.


def word_count(strng):
    strng_list = strng.split()
    return len(strng_list)
s = word_count("Hello this is string sample")
print(s)
"""

"""
# Create a function that takes a text file as input and returns
#the number of words contained in the text file.
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
 
print(count_words("filename.txt"))


#REPLACING comma with spaces

def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")   #replacing comma with space
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("filename.tx"))

#Create a script that generates a text file with all letters of the English alphabet
#inside it, one letter per line.

import string
 
with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:          #ascii use to generate a string of all letters
        file.write(letter + "\n")

"""
"""
#Printout in each line the sum of homologous items from the two sequences
a = [1,2,3]
b = (4,5,6)

for i,j in zip(a,b):     #ZIP() => method takes iterable or containers and returns a single iterator object, having mapped values from all the containers
    print(i+j)
"""

"""

#Store the dictionary in a json file.

import json
 
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
 
with open("filename.json", "w") as file:
    json.dump(d, file, indent=4)    #json.dump used to write the dictionary into file
    #indent = 4 , shows 4 white spaces

"""

"""
#Please download the file in the attachment and use Python to print out its content.

import json
from pprint import pprint
 
with open("filename.json","r") as file:
    d = json.loads(file.read())     #gets a string as output and create a dictionary object out
 
pprint(d)
"""

"""
# Add a new employee to the json file

import json

with open("filename.json","r+") as file:    #r+ use for reading and writing
    d = json.loads(file.read())
    d["employees"].append(dict(firstname = "Vikas", lastname = "Khurana"))
    file.seek(0)   #The seek () method sets the current file position in a file stream. The seek () method also returns the new postion.
    json.dumps(d, filename, indent=4, sort_keys=True)
    file.truncate()
    
"""
"""
#Enumerate=> creates an enumerate object which yields pairs of indexes and items.
#Then we iterate through that object print out the item-index pairs in each iteration together with some other strings.

a = [1, 2, 3]
for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))
"""
"""
#Create a program that prints out Hello  every two seconds.
import time
while True:
    print("Hello")
    time.sleep(2)
"""
"""
#program to print Hello repeateadly 1sec first then 2sec second interval by one
import time
i = 0
while True:
    i =i+1
    print("Hello")
    time.sleep(i)
"""

"""
import time
i=0
while True:
    print("Hello")
    i=i+1
    if i==3:
        print("End of loop")
        break
    time.sleep(i)


"""
"""
#TRY and EXCEPT
def vocab(word):
    try:
        return d[word]
    except KeyError:
        return "Input Word doesn't exist.."
d = dict(weather = "clima", earth = "terra", rain ="chuva")
word = input("Enter word").lower()
print(vocab(word))

"""
"""
#Create a script that reads this file, multiplies its values by two, and saves the output in a new text file.
import pandas
 
data = pandas.read_csv("filename.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)

"""
"""
#Please concatenate this file with this one to a single text file. The content of the output file should look like in the expected output.
import pandas
 
data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

"""

"""
#Random Password generator
import random
 
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)
"""

#creating password contain atleast one number,1uppercase letter and at least 5 character

while True:
    psw = input("Enter new password : ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw)>=5:
        print("Password Genrated")
        break
    else:
        print("Password doesn't match criteria")
        














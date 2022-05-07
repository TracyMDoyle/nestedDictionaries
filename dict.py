# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

from curses import keyname
from turtle import clear


print("**************1 Update****************")

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30

print(z)


# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. 

print("***************2 Iterate Through a List of Dictionaries**************")

students = [
    
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)


def iterateDictionary(namesOfStudents):
    for x in range(0, len(students)):
        studentnames = ""
        for key, val in students[x].items():
            studentnames +=  f'{key} - {val}, '
        print(studentnames)
        
print(iterateDictionary(students))


#  Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
print("***************3 Get Values From a List of Dictionaries**************")

def iterateDictionary2(key_name, list):
    for x in range(0, len(students)):
        for key, val in students[x].items():
            if key == key_name:
                print(val)

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))


# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
print("***************3 Iterate Through a Dictionary with List Values**************")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in dojo.items():
        print(f"{len(val)} {key.upper()}")
        for i in range (0,len(val)):
            print(val[i])

printInfo(dojo)






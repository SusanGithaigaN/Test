programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "FOR and IN": "Python's *for* and *in* constructs are extremely useful, and the first use of them we'll see is with lists. The *for* construct -- for var in list -- is a"
}

# print(programming_dictionary)

# print/select specific element from dictionary
# print(programming_dictionary["Bug"])
# print(programming_dictionary["FOR and IN"])


# adding new entries
programming_dictionary["Loop"] = "loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). "

print(programming_dictionary)

# create empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#  wipe dictionary
# programming_dictionary = {} 
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "Bugs bunny adventures"
print(programming_dictionary)


# loop through a dictionary
for thing in programming_dictionary:
  # print(thing)
  print(programming_dictionary[thing])
  

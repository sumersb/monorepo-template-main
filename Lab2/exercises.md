# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*For both the dictionary and list in python they both have some methods that are fairly descriptive but they do have methods that have names that are lacking accurate descriptions. Like the 'pop' method in both dictionary and list removes a value and returns it but it would be better to be called 'popAndGet'*

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*From my understanding dictionaries underlying data structure hash table where they link keys to values for quick access, while lists use dynamic arrays*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes I believe you can access any index in O(1) time which means you do not have to iterate over the list to retrieve the value at the 7th index with lists using the format given in the example*

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Pros: The code you write can be very versatile and reusable. It probably makes the code less complex thanks to the ability to use any data type
Cons: There are less safety rails because the code is so versatile which might make you more prone to making mistakes and your code having unintended consequences.
*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*After reading the API References I felt that the functions are well named and that you can get a good understanding of what a function is supposed to do through the name making code involving requests easier to read*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*It seems the Request method has the following parameters
method, url, headers, files, data, json, params, auth, cookies, hooks
This is a lot more than 5*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*'**kwargs' is like a variable amount of key/value pairs that can be passed in as a parameter, it could be 0+ key/value pairs making the function far more flexible in what it can take in as a parameter*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*My understanding is that the values that are set to 'None' are the ones that have a predetirmined value that can be overwritten, it simplifies the code when inputting so you don't have to always put in an input as those parameters will have a default 'None' value*

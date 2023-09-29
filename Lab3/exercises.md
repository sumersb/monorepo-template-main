# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *edit your response*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *edit your response*
1. What class does Texture inherit from?
	- Texture inherits from the image class
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- Texture inherits all attributes and methods from the Image
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I think texture has a "has-a" relationship with 'Image' because to me Texture is not an Image but it can have an image in how the texture appears.
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes Python does create a default constructor that takes no parameters

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

From my understanding threads in Python are not thread safe unless you implement something like a lock system where only one thread can operate on something that is locked at once preventing race conditions  
  

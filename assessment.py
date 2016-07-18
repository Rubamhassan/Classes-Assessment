"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
1- Encapsulation : when data lives close to its functionality like the example of the mutli-vitamin pill that has everything you need in one pill all close to each other.
2- Abstraction : like when you dont need to know the infor a method is using internally. like hiding things just to reduce the complexity of it.
3-Polymorphism : easy to use for many different types or is flexible with many functions.


2. What is a class?
A template of data and functions that are associated together andthat holds intial values that can be used in many functions. We could have parent classes and child classes. classes can be a type of thing like a string or file. classes names are written in UpperCamelCase.

3. What is an instance attribute?
Facts about the instance, variables that are part of the class.

4. What is a method?
A function in a class.

5. What is an instance in object orientation?
A specific realization of an object, created by python and then initialized


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
The class attribute is shared by all the instances of the class but the instance attribute is only for that instance.
example:
class attribute : fido =pet()
instance attribute : fido.age = 6

"""


# Parts 2 through 5:
class Student(object):

	def __init__ (self,first_name,last_name,address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
	
	# def give_info(self):
	# 	print "first_name:"%s,"last_name"%s, "address" %s (self.first_name,self.last_name,seld.address)


class Question(object):
	def __init__ (self,question,correct_answer):
		self.question = question
		self.correct_answer = correct_answer

	def ask_and_evaluate(self):
		user_answer = raw_input(self.question)
		
		if user_answer == self.correct_answer:
			return True
		else:
			return False  
	
class Exam(Question):
	def __init__ (self,name):
		self.name = name
		self.questions = []

	def add_question(self,question,correct_answer):
		self.questions.append((question,correct_answer))
		
	def administer(self):
		score = 0
		for question in self.questions:
			self.question = question[0]
			self.correct_answer = question[1]
			if super(Exam,self).ask_and_evaluate() == True:
				score = score + 1
		
		return score




# def take_test(exam,student): #write a function outside the class since its not a method


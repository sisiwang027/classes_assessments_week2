"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main advantages are abstraction, encapsulation and polymorphism.
   Abstraction means we know how to use it, and no need to know how it works internally.
   Encapsulation means put all common things together.
   Polymorphism means it's easy to meet the different.


2. What is a class?

   Class is a kind of type in python as same as function. Class has some methods and attributes
   in common. A base class can be inherited by its child class, which means its child class can 
   share all its attributes and methods. In additon, we can instantiate an object(instance) of a class. 


3. What is an instance attribute?

    instance attribute is a attribute of an instance of a class.
    For example:    class A(object):
                        class_attri = 1
                        pass
                    object_a = A()
                    object_a.class_attri = 2
    object_a.class_attri is an instance attribute. A is a class and class_attri is a class attribute.


4. What is a method?

   method is a kind of funciton in class.The first parameter is self. 
   method can be used directly by object, such as object.method(arguments).


5. What is an instance in object orientation?

   instance is an dindividual occurrence of a class.
   a = A(), this is called instantiating, a is an instance.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attribute is a attribute of the class and shared by all instances.
   Instance attribute is a attribute of an instance of a class and unique to that instance.
   Example is the same one given in question 3.

"""


# Parts 2 through 5:
# Create your classes and class methods

""" I finish these parts, but I spend half day to do it. It's not easy for me. 
I try to search how to use __repr__ on line. I am not sure its usage is correct. 
Sometimes I just try if it works or not step by step in ipython. When I finish 
the part 3, I get a more clear understanding of relationship of the classes. 
Next time, I should read the whole part before start. Knowing the whole fram 
helps me to finish the assessment. """

class Student(object):
    """Student class, store first name, laste_name and address of sutdents."""
    def __init__(self, first_name, last_name, address):
        """Initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        """return a printable representation of the object"""
        return self.first_name + " " + self.last_name


class Question(object):
    """Question class, ask questions and evaluate the results."""
    def __init__(self, question, answer):
        """Initialize Student"""
        self.question = question
        self.answer = answer

    def __repr__(self):
        """return a printable representation of the object"""
        return "<object of Question class>"

    def ask_and_evaluate(self):
        user_answer = raw_input("{} > ".format(self.question))
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """Exam class, adding questions and calculating score."""

    def __init__(self, exam_name):
        """Initialize Exam"""
        self.exam_name = exam_name
        self.questions = []

    def __repr__(self):
        """return a printable representation of the object"""
        return self.exam_name

    def add_question(self, obj_question):
        """add all objects of Question class as a list."""
        
        self.questions.append(obj_question)

    def administer(self):
        """calculating the score using the methods of questions"""
        self.all_que_num = 0
        self.corre_que_num = 0
        for que in self.questions:
            if que.ask_and_evaluate():
                self.corre_que_num += 1
                self.all_que_num += 1
            else:
                self.all_que_num += 1

        return self.corre_que_num * 100.00 / self.all_que_num

    def calculate_score(self):
        return self.corre_que_num * 100.00 / self.all_que_num


class StudentExam(object):
    """docstring for StudentExam"""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = -1

    def __repr__(self):
        """return a printable representation of the object"""
        return "{} took {}, and got {}.".format(self.student, self.exam, self.score)

    def take_test(self):

        self.score = self.exam.administer()
        print "{} took {}, and got {}.".format(self.student, self.exam, self.score)


class Quiz(Exam):
    def administer(self):
        self.all_que_num = 0
        self.corre_que_num = 0
        for que in self.questions:
            if que.ask_and_evaluate():
                self.corre_que_num += 1
                self.all_que_num += 1
            else:
                self.all_que_num += 1 
                       
        return int(round(self.corre_que_num * 1.0 / self.all_que_num))


def example():
    student = Student('sisi', 'wang', '6215')

    exam = Exam('Midterm')
    set_q0 = Question('1 + 1', '2')
    set_q1 = Question('1 + 2', '3')
    set_q2 = Question('1 + 3', '4')
    set_q3 = Question('1 + 4', '5')
    exam.add_question(set_q0)
    exam.add_question(set_q1)
    exam.add_question(set_q2)
    exam.add_question(set_q3)
    student_exam = StudentExam(student, exam)
    student_exam.take_test()

    quiz = Quiz('June')
    quiz.add_question(set_q1)
    quiz.add_question(set_q2)
    quiz.add_question(set_q3)
    student_quiz = StudentExam(student, quiz)
    student_quiz.take_test()

example()





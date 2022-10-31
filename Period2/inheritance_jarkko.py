'''
easier to inherit a class than create a new one from scratch 
basically we can add something to an existing class
sometimes its not possible to modify a class 
for example if u only have the source code 

steps for using inheritance
create a new class with the inheritance class as a parameter
def new __init__ function with old and new parameters
super().__init__ = old parameters
then self.newparameter = newparameter

in python if u want to print an object then
python will tell u the name of the class and the address in python memory
in order to print the info we want we use a special function
__str__ gives a string representation of your program
you dont need to call __str__ function as python calls it automatically
python uses string function from inherited class
then make new __str__ function to add the new parameters that u want to print
super().__str__() + "[" + self.color + "]" 
this will call old string function and then add [color] to the print output

we can inherit class variables too

external interface
application programmer interface = API
how we question a server from an application
every service may use a different api
'''
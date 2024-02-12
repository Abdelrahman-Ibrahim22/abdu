#In Python, square brackets [ ] serve multiple functions, including:
#Indexing: They are used for indexing or accessing elements from a sequence type like a list, tuple, or string by their position. For example, my_list[0] accesses the first element of my_list
print ("Good mornning"[5])
print ("Octucode" [3])
#The len() function in Python returns the number of items in an object
#For example, it can return the number of characters in a string, the number of items in a list, or the number of keys in a dictionary.
print (len("OctoCode"))
# len can not used to count the number of an integer Ex: print (len (12345)), will give you a type error.
#The `str()` function in Python converts the given object into a string representation.
str (1234567)
print (len (str(1234567)))
#Anything the user enter in an input function is converted directly into string.
User_Pin = input("Enter your pin number: \n")
print (len (User_Pin))
#type function let you know the type of any data
print (type(User_Pin))
#How could I let the user enter his two-digits code and then I convert this string ,as the input function convert the input into string, then apply an addition equation on it? 
user_code= input("please enter your two digits code \n")
first_number= int(user_code [0]) # Remeber: we always count from zero, here it like I say index the first number and convert it into integer
second_number= int (user_code[1]) # same as above create a varaible in which you index the second number and convert it to integer
print (first_number+ second_number) #Add the two variables in the folder
#please excuse my dear aunt sally where p=paranthases, e= exponental, m=multiplication, d=division, a= addition, s=substraction
#above is how the processes over the number are arranged. Remeber the math processes also follow the order from left to right, I mean if you have addition and substraction, and the substraction comes on the left side before the addition, the substraction will performed first, and then the addition. The same rule applied to multiplication and division if the division comes first on the left side it is applied first. See the example below.
print (2**3) #this is the exponentail
print (3*2-6 + 9/3) #this gives you 3.0 (a float) not -3 as substraction are performed before addition from left to right.
#the function of the floor division sign (//) is to devide and give you the integer number only out of the calculation.
print(10//3) #should give 3 and neglect the remaining 1 or any decimal in general.
# if you want to know ((only)) the remaining of a function and neglect the integer you should use the % sign.
print(10%3) #should give you 1. 



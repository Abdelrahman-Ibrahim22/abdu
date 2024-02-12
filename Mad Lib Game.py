color=  input ("Enter your color: \n")
plural_noun=  (input("Enter a plural noun: \n"))
celebrity=  input ("Enter your favourite celebrity name: \n")
print ("Roses are " + color +"\n" + plural_noun + " are blue" + "\n" + "I love " + celebrity)
#Working with functions, and using return
def cube (num) :
    return num * num *num
print (cube (7))
#If statement
is_male= False
if is_male:
    print ("You are a male")
else:
    print ("You are a female")
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
      return num1
    elif num2 >= num1 and num2>= num3 :
       return num2
    else :
     return num3
print (max_num(3, 40, 5))   

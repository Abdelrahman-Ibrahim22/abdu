room_length= input ("Please enter your room Length : \n")
room_width= input ("Please enter your room width : \n")
#convert the data type from string, the result of the input is always string, to float. It is better to convert to float as the user might enter decimals in the calculations.
length= (float(room_length))
width= (float(room_width))
#create a varialble that calculate the area of the room (rectangle)
area= length*width
#if you tried to print the area now, you will have a typeError; as the result of the area variable is a float and Python can print only one data type. So first convert the area to string.
str_area= str(area)
print ("The total area is :  " + str_area ) #remember not to enter the varable area but the str(area) so that you get a complete string line that could be calculated.
#Calculate painting costs, you see the project repeating twice because it reads the above lines too.
room_length= input ("Please enter you room length : \n")
room_width= input ("Please enter your room width : \n")
#convert type
float_length= float(room_length)
float_width= float(room_width)
#calculate the room area
area= (float_length*float_width)
#convert the area into string to avoid concatenation
str_area= str(area)
print ("the total area is : " + str_area)
meter_cost= input ("How much for 1 meter? : \n")
#convert type
float_metercost= float(meter_cost)
#calculate the total costs by multiply area* float_metercost variables
total_costs= (area * float_metercost)
#convert the total cost into string to avoid concatenation error
str_totalcosts= str(total_costs)
print ("Give the guy : "+ str_totalcosts +"$")



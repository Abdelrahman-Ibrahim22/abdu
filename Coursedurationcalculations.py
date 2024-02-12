course_duration = input("Please enter your course duration in seconds: \n")
# Convert type into int
int_duration = int(course_duration)
# Calculate the number of course hours
hours = int_duration // 3600  # Floor division sign // gives you the integer number only
remaining_seconds_after_hours = int_duration % 3600  # Seconds remaining after calculating hours
# Calculate the number of minutes
minutes = remaining_seconds_after_hours // 60  # Convert the remaining seconds into minutes
# Calculate the remaining seconds after calculating minutes
seconds = remaining_seconds_after_hours % 60  # Remaining seconds after calculating minutes

print("This course is " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds")


  
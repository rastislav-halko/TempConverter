
# DECIMAL NOT ACURATE - FIX IT

#1. prompt user to enter the temperature in an integer form (decimals not allowed):
temp_F = input('Enter temperature in Fahrenheit: ')

#2. convert string input entered by user to a number (integer):
temp_F_float = float(temp_F)

#3. convert the miles-to-km multiplier from string to float:
formula = (temp_F_float - 32) * 5/9

#4. actual conversion:
C_value = (temp_F_float * formula)

# Final output prints out the amount of miles entered by the user in the form of a string (since we are using the miles variable instead of miles_float) plus value of kilometers converted from float back to a string. Finally the word kilometers is added to conclude the output:
print(str(temp_F_float) + ' F equals ' + str(C_value) + ' C.')

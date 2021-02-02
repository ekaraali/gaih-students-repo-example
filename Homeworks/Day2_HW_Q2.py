# Ask user to provide a single digit input
n = int(input("Please enter a single digit integer: "))

if (n > 9 or n < 0):

 print("Please enter an integer between 0-9")

else:
 even_numbers = [i for i in range(0,n+1) if i % 2 == 0]
 print(even_numbers)
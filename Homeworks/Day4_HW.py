#Find prime numbers between between 0 and 100
def prime_number(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True
    else:
      for i in range(2, number):

          #if any i value is divisible by the current number, than return False
         if (number%i == 0):
            return False
      #if none of i value is divisible by the current number, than return True
      return True

#add all prime number into a list
prime_numbers_list = list()
for i in range(1,101):

    if (prime_number(i)):
        #when true returns in the function, then append numnber to the list
        prime_numbers_list.append(i)

#display the prime numbers on the screen
print("Prime numbers between 0 and 100 are:",prime_numbers_list)
# ---------------------------------------------------------------------------------------------------
# ======================================== Ans: A ===================================================
# ---------------------------------------------------------------------------------------------------
# ====================Ans: A-1

# Use of for loop to print all numbers from 1 to 10
for i in range(1,11):
    print(i)





# ====================Ans: A-2

# printing all numbers from 1 to 10. We declare a variable and then initialize it to 1, then when the loop run, we increament this
# variable by one and print it. We stop the loop as soon as it is just below 11
i=1
while (i<11):
    print(i)
    i+=1





# ====================Ans: A-3a
# Printing all number from 1 to 10 except 5 by using continue control statement
for i in range(1,10):
    # if i==5, then skip the current iteration
    if(i==5):
        continue
    print(i)





# ====================Ans: A-3b
# Printing all numbers starting from one using a loop and then terminating the loop as soon as the number is equal to 7
for i in range(1,10):
    # Break the loop when i==7
    if(i==7):
        break
    print(i)














# ---------------------------------------------------------------------------------------------------
# ======================================== Ans: B ===================================================
# ---------------------------------------------------------------------------------------------------


# ====================Ans: B-4
# Looping through the contents of a list
fruits=["apple", "banana", "cherry", "date", "fig"]
for fruit in fruits:
    print(fruit)


# ====================Ans: B-5
# Printing all characters in a given string
iteration_string=input("Enter a string, We will print out its characters! ")
# the variable "char" in the for loop will recieve a character for each iteration of the loop until all the characters
# in the given string are completed
for char in iteration_string:
    print(char)





# ====================Ans: B-6
# Counting the number of times a appears in a string

a_count_string= input("Enter a Word. We will count the number of times the character \"a\" has appeared in it! ")
# # Initialize an accumulator varible that will be incremented every time "a" is found in the given Word/String
a_count=0
for char in a_count_string:
    # The character "a" can be either capital or small
    if (char=='a' or char=='A'):
        a_count+=1
print("'A/a' appeared ",a_count, " times in: ",a_count_string)











# ---------------------------------------------------------------------------------------------------
# ======================================== Ans: C ===================================================
# ---------------------------------------------------------------------------------------------------

# ====================Ans: C-7
# printing multiplication table from 1 to 5

# For each "outer loop", i will recieve a number from 1 to 5,
# We will run a "inner loop" for each iteration of "outer" loop that will iterate 10 times
# In the "inner" loop, we will simply multiply the outer loop control variable and inner loop control variable and print the result
for i in range(1,6):
    print("===================Table of ",i)
    for j in range(1,11):
        print(i,"x", j," = ",i*j)
    print('\n')






# ====================Ans: C-8
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
for i in range(1, 6):
    for j in range(0,i):
        print("*", end="")
    print('')













# ---------------------------------------------------------------------------------------------------
# ======================================== Ans: D ===================================================
# ---------------------------------------------------------------------------------------------------

# ====================Ans: D-9
# Calculating sum of all even numbers from 1 to 100
# the 3rd argument to range function is called step, this is used to skip numbers in a range
# A skip of '2' in a range of 0 to 101, will give us numbers 0,2,4.....98,100.
# The 'total' variable acts as accumulator and will be incremented with next even number upon each iteration
total = 0
for even_number in range(0,101,2):
    total+=even_number

print("The sum of even numbers from 1 to 100 is: ", total)





# ====================Ans: D-10
# Prime number check

# if a number is divisible by a given number, then the remainder is 0.
# As it is known that every number is divisible by 1 and itself, So,
# We will loop from 2 to 1 less than the given input number and on each iteration, divide the number by the iteration value of the loop
# After each division, we will check if the remainder is 0, if it is then the number is not prime and we will end the loop using 'break'.
# If the loop ends without finding a remainder 0, then we declare the number to be a prime number
number = int(input("Enter a number and we will guess whether it is prime or not! "))
isPrime=True
for i in range(2,number):
    if(number%i==0):
        print(number, " is not a prime number!")
        isPrime=False
        break
if(isPrime):
    print("Congratulations!!! you have found a prime number. ",number," is a prime number!")





# ====================Ans: D-11

# Printing first 10 fibonacci sequence

# Fibonacci is a sequence where starting at 0 and 1, the sum of previous and current number gives the next fabonacci number
# Starting values of the Fibonacci sequence
previous, current = 0, 1

# Print the first 10 terms
print("First 10 terms of the Fibonacci sequence:")
for i in range(10):
    # print out the current number
    print(previous, end=" ")

    # calculate the next fabonacci number in the sequence 
    next = previous + current
    # update the 'previous' variable so that it moves farward
    previous = current
    # update the 'current' variable so that it too moves to point to the 'next' fabonacci number in the sequece
    current = next












# ---------------------------------------------------------------------------------------------------
# ======================================== Ans: E ===================================================
# ---------------------------------------------------------------------------------------------------

# ====================Ans: E-12
# Factorial calculation

# Calculation of factorial of user input integer number
fact_number=int(input("Enter an integer number and we will calculate its factorial! "))

# # this variable will be used to keep track of the while loop. When this variable is equal to 0, while loop is stopped
base=fact_number

# # this is accumulator variable that will accumulate the product of the factorials
factorial=1
while (base!=0):
    # Factorial is calculated by multiplying a number recursively with previous numbers.
    factorial= factorial*base
    base-=1
print(factorial)





# ====================Ans: E-13
# Finding the Largest Number:
print("\nEnter a List of integer numbers and we will find out the maximum without using built in functions!\n")
numbers=[]
while True:
    user_input=input("Enter Integer number(X/x to finish List): ")
    # If use finished entering more numbers, terminate the loop
    if (user_input=='X' or user_input=='x'):
        break
    numbers.append(int(user_input))

max=numbers[0]
for number in numbers:
    # If a number is greater than the max, just replace it.
    if(number>max):
        max=number

# The number contained in 'max' is the largest one after the loop ends
print("The largest number is: ", max)

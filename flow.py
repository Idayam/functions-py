# Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50. 
def even_numbers():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)


# Write a function that takes an integer argument and prints
#  "Prime" if the number is prime, and "Not prime" if the number is not prime.
def integer_numbers(b):
    if b>1:
        for i in(2,b):
            if b%i==0:
                print(f"{b} prime")
                break
        else:
            print(f"{b}not prime")
        



# Write a function that takes a list of integers as input and prints
#  the sum of all the even numbers in the list.
def integers(numbers):
    sum=0
    for i in numbers:
       if i%2==0:
        sum+=i
    print(sum)



# Write a function that takes any two integers as input, and prints the sum of all the numbers
#  between the two integers (inclusive) that are divisible by 3.
def intergers(a,b):
    x=range(a,b)
    sum=0
    for i in x:
        if i%3==0:
           sum+=i
    print(sum)

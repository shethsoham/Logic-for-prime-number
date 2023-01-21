

#find out if the number is prime or not
def prime_checker(number):
    for i in range(2,int(number/2)+1):


        if number % i == 0 :
            print(number,"is not a prime number ")
            break
    else:
        print(number,"is a prime number")



n = int(input("enter the number yoyu want to check  : "))
if n == 1:
    print("It is prime number")
else :
    prime_checker(number = n)
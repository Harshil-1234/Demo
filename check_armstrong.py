def check_armstrong(n):
    s=0
    m=n
    while m!=0:
        s=s+(m%10)**3
        m=m//10
    if s==n:
        print("Given number is Armstrong number")
    else:
        print("Given number is not Armstrong number")
n=int(input("Enter any numer"))
check_armstrong(n)

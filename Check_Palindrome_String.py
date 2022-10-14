print("Enter the string you want to check for Palindrome")
string = input()
first,chk = 0 ,0
last = len(string) - 1

while(first<=last):
    if(string[first] == string[last]):
        first += 1
        last -= 1
    else: 
        chk += 1
        break

if(chk==0):
    print("The given string IS a Palindrome")
else:
    print("The given string IS NOT a Palindrome")
#Write a python program to reverse a number using a while loop.

num=int(input("Enter a number to reverse:"))
temp = num
reverse =0


while(num>0):
    digit = num%10              
    reverse=(reverse*10)+digit    
    num=int(num/10)
print(reverse)

#Write a python program to check whether a number is palindrome or not?

if(reverse==temp):
    print("Palindrome number")
else:
    print("Not a palindrome number")

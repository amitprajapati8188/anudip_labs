#Python program to check if the given string is a palindrome 

def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

word = str(input("Enter a string: "))

if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


#Python program to check if a given number is an Armstrong number

given_number = int(input("Enter a number"))

given_number=str(given_number)

string_length = len(given_number)
sum=0

for i in given_number:
    sum+=int(i)**string_length

if sum==int(given_number):
    print("Armstrong number")
else:
    print("Not armstrong no")

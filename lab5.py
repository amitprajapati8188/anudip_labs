#Accept a name from the user and display that in lower case using lower() function

name = str(input("Enter the name:"))
lower_TEXT = name.lower()
print(lower_TEXT)

#Write a function that takes one argument and returns 'Positive' if the number is greater than 0,  
# 'Negative' if it's less than 0, and 'Zero' if it's 0.Test it with different numbers .

def cheak_num(x):
    if(x>0):
        print("positive")
    elif(x<0):
        print("negetive")
    else:
        print("it is zero.")

number = int(input("Enter the number:"))
cheak_num(number)
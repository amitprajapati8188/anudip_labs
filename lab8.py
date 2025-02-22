#WAP to print count of uppercase, lowercase, numbers and special characters in a string.

#print count seperately.

'''str = "App dev using pyhton !! 2025"
print("my string:",str)

upr=0
lwr=0
num=0
spl=0

for i in range(len(str)):
    if str[i]>='A' and str[i]<='Z':
        upr+=1
    elif str[i]>='a' and str[i]<='z':
        lwr+=1
    elif str[i]>='0' and str[i]<='9':
        num+=1
    else:
        spl+=1


print("Uppercase letters : ",upr)
print("Lowercase letters : ",lwr)
print("Numbers : ",num)
print("Special chacters ",spl)'''


#WAP deducing multiple string methods.

import base64

text = "Hello, World!"
encoded_text = base64.b64encode(text.encode('utf-8'))
decoded_text = base64.b64decode(encoded_text.decode('utf-8'))
print("encoded text : ",encoded_text)
print("decoded text : ",decoded_text)

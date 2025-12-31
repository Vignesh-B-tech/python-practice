#Reverse a string 
#1.using loop concept

a="watermelon"
b=""
for i in a:
   b=i+b 
print(b)

#2.using Slicing method
a="watermelon"
b=a[::-1]
print(b)
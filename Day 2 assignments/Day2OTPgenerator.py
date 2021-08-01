#Assignment 2
#OTP GENERATOR 8 DIGIT
import string
import random
ch=string.ascii_letters+string.digits
length=8
OTP=''
for i in range(0,length):
  OTP=OTP+ random.choice(ch)
print("OTP:",OTP)
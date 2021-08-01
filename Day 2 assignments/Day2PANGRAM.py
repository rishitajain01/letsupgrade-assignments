#Assignment 2
#Q2)Check whether a string is a pangram.
import string
ch=set(string.ascii_lowercase)
sent=input("enter your sentence")
if(set(sent.lower()) >= ch):
  print("pangram")
else:
  print("non-pangram")
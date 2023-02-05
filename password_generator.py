import random
import string

length=(int(input("enter a lenth of password ")))


capital_letters= string.ascii_uppercase
#it gives capitalsletters

small_letters= string.ascii_lowercase
#it gives small letters
digit=string.digits
#it gives digits from 0 to 9
symbols=string.punctuation
#it gives symbols and puncuation
all= capital_letters+small_letters+digit+symbols
#it adds all the character and symbols
temp=random.sample(all,length)
#it gets random value from the list
password=''.join(temp)
#It then gets a random value from this list to create a password which is ''.join(temp)
print(password)
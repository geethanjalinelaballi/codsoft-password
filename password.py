
import string
import random

all_characters = string.ascii_letters + string.digits + string.punctuation

length_of_password = int(input("Enter the length of the password: "))

password = ''.join(random.choices(all_characters, k=length_of_password))

print("Generated password is:", password)



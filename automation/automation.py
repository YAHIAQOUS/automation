import re

with open('assets/potential-contacts.txt','r') as file:
    text = file.read()
print (text)

phone_numbers = re.findall('[0-9]+[-]*',text)
print (phone_numbers)
with open('assets/phone_numbers.txt','w') as file:
    file.write(str(phone_numbers))

emails = re.findall('[1-9a-z]*@[a-z]*.[a-z]*',text)
print(emails)
with open('assets/emails.txt','w') as file:
    file.write(str(emails))

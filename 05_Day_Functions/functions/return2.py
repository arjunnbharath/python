def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last

a =input ("enter your first name")
b =input ("enter your last name")
Fullname=create_name(a,b)
print (Fullname)
#To Validate a Phone number and Email
import re

def validate(pattern, string):
    return bool(re.fullmatch(pattern, string))

phone_pattern = r'^(\+91[\s-]?)?[6789]\d{9}$'
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

phone = input("Enter phone number: ")
email = input("Enter email ID: ")

print("Valid phone number" if validate(phone_pattern, phone) else "Invalid phone number")
print("Valid email ID" if validate(email_pattern, email) else "Invalid email ID")
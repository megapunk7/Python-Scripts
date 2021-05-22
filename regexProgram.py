import re
text = input()
office_phoneRegex = re.compile(r'''
    \d\d
    (-)?
    \d\d\d\d\d\d\d
    ''',re.VERBOSE) #01-41000042, 014100002, 41000002

mobile_phoneRegex = re.compile(r'\d{10}') #9840173413

emailRegex = re.compile(r'''
    [a-zA-Z0-9._]+
    @
    [a-zA-Z0-9._]+
    ''', re.VERBOSE) #secretary@moha.gov.np

extracted_office_no = office_phoneRegex.findall(text)
extracted_mobile_no = mobile_phoneRegex.findall(text)
extracted_emails = emailRegex.findall(text)

print(extracted_emails)
print(extracted_mobile_no)
print(extracted_office_no)
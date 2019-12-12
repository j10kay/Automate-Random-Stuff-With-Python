#! python3
import re, pyperclip

phoneRegex = re.compile(r"""
# 202-717-2989, 717-2989, (202) 717-2989, 717-2989 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                       # first separator 
\d\d\d                       # first 3 digits 
-                            # separator
\d\d\d\d                     # last 4 digits
(((ext(\.)?\s) | x)          # extension word-part(optional)
(\d{2,5}))?                  # extension number-part (optional)   
)
""", re.VERBOSE)

emailRegex = re.compile(r"""
#some.+_thing@some.+_thing.com
[a-zA-Z0-9_.+]+    # name part
@                 # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

""", re.VERBOSE)

text = pyperclip.paste()
extractedPhoneNumbers = phoneRegex.findall(text)
extractedEmailAddresses = emailRegex.findall(text)
allPhoneNumbers = []
for phoneNumber in extractedPhoneNumbers:
    allPhoneNumbers.append(phoneNumber[0])

results = "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractedEmailAddresses)
pyperclip.copy(results)

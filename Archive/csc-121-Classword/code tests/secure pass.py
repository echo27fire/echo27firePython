password = 'ILOVEPYTON'

if password.isalpha():
    print('invalid, just contain one number.')
elif password.isdigit():
    print('Invalid, must have one non-numiric character')
elif password.isupper():
    print('Invalid, password cannot be all upper case.')
else:
    print('password is secure')





special = '1357 Country Ln.'
s_string = special[4:]

print({s_string})

mystr = 'yes'
yourstr = 'no'
mystr += yourstr
print(mystr)

def isPhoneNumber(text):# 'text' is the only parameter we need to judge the identity of given text.
# Define some rules for a US phone number.
# For a phone number distributed by US-based tele companies, the basic structure would be:
# (+1) 888-888-8888, in which we can just elude the (+1) part, for the cause of convenience.
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True # If all the above conditions leads to 'False' are not met, we arrive in 'True'. 

  message='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(0,len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        nums.append(chunk)
print(nums)
  

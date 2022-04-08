import re
from validate_email import validate_email
import validators

def is_string_an_url(url_string: str) -> bool:
    result = validators.url(url_string)
    return result

def check_blank(word0,word1,word2,word3):
    if word0 == "" or word1 == "" or word2 == "" or word3 == "":
        return False
    else:
        return True

def check_blank2(word0,word1,word2,word3,word4,word5,word6,word7,word8,word9,word10,word11,word12):
    if word0 == "" or word1 == "" or word2 == "" or word3 == "" or word4 == "" or word5 == "" or word6 == ""  or word7 == "" or word8 == "" or word9 == ""  or word10 == "" or word11 == "" or word12 == "":
        return False
    else:
        return True

def check_blank3(word0, word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13):
    if word0 == "" or word1 == "" or word2 == "" or word3 == "" or word4 == "" or word5 == "" or word6 == "" or word7 == "" or word8 == "" or word9 == "" or word10 == "" or word11 == "" or word12 == "" or word13 == "":
        return False
    else: 
        return True       

def checker(pas):
    if(len(pas)<8):
        return False

    stringArray = list(pas)

    digitFlag = False
    symbolFlag = False
    upperFlag = False

    for i in stringArray:
        if re.match('\d', i):
           digitFlag = True

        if re.match('[A-Z]', i):
            upperFlag = True

        if re.match('[ -/:-@[-`{-~]', i):
            symbolFlag = True


    if digitFlag == True and upperFlag == True and symbolFlag == True:
        return True
    else:
        return False

def valemail(email):
    
    is_valid = validate_email(email_address = email, check_format = True)

    if is_valid is True:
        return True
    else: 
        return False

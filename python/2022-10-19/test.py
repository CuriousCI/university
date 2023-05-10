from timeit import Timer
from re import match

password = 'Aa@09asng2'
password = 'Aa@09asng2Aa@0'
# password = 'Aa@09asng2/'
# password = ''


def check_pwd_re(pwd: str) -> bool:
    return bool(match('(?=^[a-zA-Z\d9$#@]*$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])', pwd)) and 6 <= len(pwd) <= 16


def check_pwd_re_g(pwd: str) -> bool:
    if len(pwd) < 6 or len(pwd) > 16:
        return False
    return bool(match('(?=^[a-zA-Z\d9$#@]*$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])', pwd))


def check_pwd(pwd: str) -> bool:
    if len(pwd) < 6 or len(pwd) > 16:
        return False
    condizioni = [0, 0, 0, 0]
    for x in pwd:
        if x in "abcdefghilmnopqrstuvz":
            condizioni[0] = 1
        elif x in "abcdefghilmnopqrstuvz".upper():
            condizioni[1] = 1
        elif x in "0123456789":
            condizioni[2] = 1
        elif x in "$#@":
            condizioni[3] = 1
        if x not in "abcdefghilmnopqrstuvz"+"abcdefghilmnopqrstuvz".upper()+"0123456789"+"$#@":
            return False
    return 0 not in condizioni


def check_pwd_g(pwd: str) -> bool:
    if len(pwd) < 6 or len(pwd) > 16:
        return False
    condizioni = [0, 0, 0, 0]
    for x in pwd:
        if x in "abcdefghilmnopqrstuvz":
            condizioni[0] = 1
        elif x in "abcdefghilmnopqrstuvz".upper():
            condizioni[1] = 1
        elif x in "0123456789":
            condizioni[2] = 1
        elif x in "$#@":
            condizioni[3] = 1
        if 0 not in condizioni:
            return True
        if x not in "abcdefghilmnopqrstuvz"+"abcdefghilmnopqrstuvz".upper()+"0123456789"+"$#@":
            return False
    return 0 not in condizioni


def check_pwd_2_g(pwd: str) -> bool:
    alphabet = "abcdefghilmnopqrstuvwxyz"
    if len(pwd) < 6 or len(pwd) > 16:
        return False
    check = [0, 0, 0, 0]
    for let in pwd:
        if let in alphabet:
            check[0] = 1
        elif let in alphabet.upper():
            check[1] = 1
        elif let in "0123456789":
            check[2] = 1
        elif let in "$#@":
            check[3] = 1
        else:
            return False
    if 0 not in check:
        return True
    else:
        return False


b1 = Timer(lambda: check_pwd_re(password)).repeat(1, 100000)
b2 = Timer(lambda: check_pwd_re_g(password)).repeat(1, 100000)
b3 = Timer(lambda: check_pwd(password)).repeat(1, 100000)
b4 = Timer(lambda: check_pwd_g(password)).repeat(1, 100000)
b5 = Timer(lambda: check_pwd_2_g(password)).repeat(1, 100000)

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def compare_passwd(_password):
    if _password == "happychance":
        return True
    else:
        print("That password is incorrect")
        sys.exit(0)
        return False
def arg111(potential_flag):
    return arg122(potential_flag.decode(), "rapscallion")
def enter_user_value():
    return input("Please enter correct password for flag: ")
def read_the_flag():
    return open('flag.txt.enc', 'rb').read()
def print_welcome_phrase():
    print("Welcome back... your flag, user: ")
def arg122(_password, keyword):
    keyword_modified = keyword
    i = 0
    while len(keyword_modified) < len(_password):
        keyword_modified = keyword_modified + keyword[i]
        i = (i + 1) % len(keyword)
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(_password,keyword_modified)])
potential_flag = read_the_flag()
_password = enter_user_value()
compare_passwd(_password)
print_welcome_phrase()
keyword = arg111(potential_flag)
print(keyword)
sys.exit(0)



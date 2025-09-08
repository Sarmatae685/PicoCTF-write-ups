a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

arg432 = a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]
print(f"arg432 : {arg432}, len(arg432) : {len(arg432)}") # happychance


arg232 = a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
    a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
    a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
    a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94] # Please enter correct password for flag:
print(f"arg232 : {arg232}")

arg112 = a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
    a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
    a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25]
print(f"arg112 : {arg112}") #Welcome back... your flag, user:

arg122_func_second_value = a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+a[75]+a[72]+a[78]+a[77]
print(f"arg122_func_second_value : {arg122_func_second_value}") #rapscallion


#збережемо копію функції
# def arg122(arg432, arg423): #def arg122(arg432, arg423):
#     arg433 = arg423
#     i = 0
#     while len(arg433) < len(arg432):
#         arg433 = arg433 + arg423[i]
#         i = (i + 1) % len(arg423)
#     return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
# arg444 = arg132()
# arg432 = arg232()
# arg133(arg432)
# arg112()
# arg423 = arg111(arg444)
# print(arg423)
# sys.exit(0)


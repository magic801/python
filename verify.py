import re

reg = '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'

def check_string(re_exp, str):
    res = re.search(re_exp, str)
    return res

if check_string(reg, "2012-03-041"):
    print('yes.')
else:
    print('please enter as: 2012-03-04')
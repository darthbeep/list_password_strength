import string
import math
lower = string.lowercase
upper = string.uppercase
numbers = string.digits
other = ".?!&#,;:-_*"

def minimum(password):
    l = len([x for x in lower if x in password ]) > 0
    u = len([x for x in upper if x in password ]) > 0
    n = len([x for x in numbers if x in password ]) > 0
    print l, u, n
    return l and u and n

def strength(password):
    l = len([x for x in lower if x in password ])
    u = len([x for x in upper if x in password ])
    n = len([x for x in numbers if x in password ])
    o = len([x for x in other if x in password ])
    ret = math.sqrt(l) + math.sqrt(u) + math.sqrt(n) + math.sqrt(o)
    ret = ret * 10 / len(password)
    print ret
    return ret

strength("abcD")
strength("password")
strength("helpM3!")
strength("aBCd")


import random

l = []
def random_list(n):
    for i in range(1,n+1):
        l.append(random.randint(1,100))
    return l

def average(lt):
    s=0
    for i in range(0, len(lt)):
        s+=lt[i]
    return round(s/len(lt))

def only_odd(lt):
    for i in range(1,len(lt)):
        if lt[i]%2==1:
            l.append(lt[i])
    return l

def to_str(lt):
    s="["

    for i in range(0,len(lt)):
        s+=str(lt[i])
        s+="," if i!=len(lt)-1 else ""
    s+="]"
    return s


def has_duplicates(lt):
    for i in lt:
        if lt.count(i) > 1:
            return True
    return False


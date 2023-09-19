
def concat(s,n):
    ans=""
    for i in range(1,n+1):
        ans = ans + s

    return ans

def count(s,x):
    count=0
    for i in range(1,len(s)):
        if x==s[i]:
            count+=1
    return count

def reverse(s):
    r=-1
    ans=""
    for i in range(1,len(s)+1):
        ans+=s[r]
        r-=1
    return ans

def first_last(s):
    return s[0], s[-1]


def has_two_X(s):
    count=0
    for i in range(0,len(s)):
        if s[i]=='X':
            count+=1
    return True if count==2 else False


def has_duplicates(s):
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if i!=j and s[i].lower()==s[j].lower():
                return True
    return False



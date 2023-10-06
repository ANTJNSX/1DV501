
def is_increasing(lst):
    for i in range(len(lst)):
        if i != 0 and lst[i] < lst[i-1] or lst[i] == lst[i-1]:
            return False
    return True


lst = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(is_increasing(lst))

''''
Pseudo code notes

# loop over A adding 1 each rotation
    # loop over B adding 1 each rotation
        # loop over C adding 1 each rotation
            # loop over D adding 1 each rotation
                # Check if DCBA == 4 * ABCD
'''


def get_number(a, b, c, d):
    abcd = int(str(a)+str(b)+str(c)+str(d))
    return abcd


for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                concat_str = int(str(d)+str(c)+str(b)+str(a))
                if concat_str == 4 * get_number(a, b, c, d):
                    print(F"a: {a}\nb: {b}\nc: {c}\nd: {d}\n")

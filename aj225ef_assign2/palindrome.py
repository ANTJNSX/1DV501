
ts = input("Enter a sentence that might be a palindrome: ")


def is_palindrome(s):
    chr_list = [' ', '!', '.', ',', '?']
    for char in chr_list:
        s = s.replace(char, "")

    sr = s[::-1]

    print("Input reversed:", sr)

    sr = sr.lower()
    s = s.lower()
    print("Sentence without spaces and lower:", sr)

    if s.lower() == sr:
        return True
    return False


print(is_palindrome(ts))

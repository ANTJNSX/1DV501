from list_functions import random_list, average, only_odd, to_str, has_duplicates

test_list = [1,2,3,4,5,6,7,8,9,10,1]

print("This is the test list:",test_list, end="\n")

print("\nhere is a list of 7 numbers from 1-100:", *random_list(7))

print("\nhere is the average of the test list:", average(test_list))

print("\nhere are only the odd numbers:", only_odd(test_list))

print("\nhere is the list as a string:", to_str(test_list))

print("\nhere we check if the list has duplicates:", has_duplicates(test_list))

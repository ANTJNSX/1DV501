from string_function import concat, count, reverse, first_last, has_two_X, has_duplicates


print(concat("Hello world! ", 5))

print("there are", count("hello", 'l'), "l's in hello")

print("Hello reversed is:", reverse("Hello"))

print("the first and last characters in the string Hello are:",*first_last("Hello"))

print("does the word Existential have 2 X's?:",has_two_X("Existential"))

print("does the word Existential have any duplicates?", has_duplicates("Existential"))

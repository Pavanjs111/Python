import re
def multi_char_find(test_pattern,test_char):
    for pat in test_pattern:
        print("seaching for pattern",pat)
        print(re.findall(pat,test_char))

test_char="I am her to conquer the world with a lot of power and take all the responsiblity and keep people where they belong"
test_pattern=['/D+']
multi_char_find(test_pattern,test_char)
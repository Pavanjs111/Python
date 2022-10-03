import re
def multi_char_find(test_patterns,test_chars):
    for pat in test_patterns:
        print("searching for pattern->",pat)
        print(re.findall(pat,test_chars))

test_chars="aaabbbb......abababaaabbbaaaabbbbaaabb.....aabbbbbabababb.....aaaaaabbbbbbb"
# test_patterns=['a*']
test_patterns=['ba+']

multi_char_find(test_patterns,test_chars)
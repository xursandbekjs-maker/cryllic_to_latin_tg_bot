# import transliterate
from transliterate import to_cyrillic, to_latin
# print(to_cyrillic("Assalomu alaykum"))
# print(to_latin("Ассалому алайкум"))
# print(to_cyrillic("O'zbekiston mening vatanim"))
# string.ascii()
# print("Assalom".isascii())
# print("Калайсиз".isascii())
s = input()
if s.isascii():
    print(to_cyrillic(s))
else:    
    print(to_latin(s))
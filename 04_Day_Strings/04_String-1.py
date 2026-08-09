# # 1. Single characters and length
# letter = "p"                 # Python has no separate 'char' type, this is just a string of length 1
# print(letter)                # prints: p
# print(len(letter))           # len() counts characters -> prints: 1
#
# # 2. Multi-line strings
# multi_string = """hi i am arjun.
# how r u.
# where r u from."""           # triple quotes let the string span multiple lines as typed
# print(multi_string)          # prints all 3 lines exactly, with real line breaks
#
# # 3. String concatenation
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '                  # just a string holding one space character
# full_name = first_name + space + last_name   # + joins strings together (like JS)
#
# print(first_name)            # prints: Asabeneh
# print(last_name)             # prints: Yetayeh
# print(full_name)             # prints: Asabeneh Yetayeh
# print(len(first_name))       # counts letters in "Asabeneh" -> prints: 8
#
# # 4. Escape sequences
# print('Hello\nWorld')        # \n = newline -> Hello and World print on separate lines
# print('Day 1\t5\t5')         # \t = tab -> spaces out values like columns
# print('Day 2\t6\t20')        # same tab spacing, second row
# print('This is a backslash symbol (\\)')   # \\ = one literal backslash (needs escaping)
# print('In every programming language it starts with \"Hello, World!\"')  # \" = literal double-quote inside the string


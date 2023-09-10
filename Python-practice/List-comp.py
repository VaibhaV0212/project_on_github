# my_list = ['apple','banana','cherry','neem']
# b = []
# c = []
# for i in my_list:
#     if i.startswith('a'):
#         b.append(i)
#     else:
#         c.append(i)
# # print(f'b=> {b}')
# # print(f'c=> {c}')


# # -------- List Comprehsion ------
# w =[]
# z = []

# x = [w.append(i) if i.startswith('a') else z.append(i) for i in my_list]
# # print(f'w=> {w}')
# # print(f'z=> {z}')

# --------- Regex -----------------------------

import re

# --------------- 1 -----------
# pattern = '^v.....v$'
# user = input('Enter to search : ')
# result = re.match(pattern, user)
# if result: print('Success')
# else: print('Not success!')


'''
Regex meta charater :   [ ] . ^ $ * + ? { } ( ) \ | 

[] = specifies a set of characters you wish to match
*  = Matches zero or more occurences of the pattern left to it
+  = Matches one or more occurences of the pattern left to it
?  = Matches zero or one occurence of the pattern left to it
{} = This means at least n, at most m, repetitions of the pattern. 
() = (a|b|c)xy, match any string  that matches either a, b or c followed by xy
'''


# --------------- 2 -----------
# pattern = r"[abc]"
# user = input('Enter to search : ')
# # result = re.match(pattern, user)
# # result = re.findall(pattern, user)
# result = re.search(pattern, user)
# print(result)
# if result: print('Success')
# else: print('Not success!')

# ---------------- 3 --------------
# a{2,3} 


# ---------------- 4 ---------------
# a{2,3} 


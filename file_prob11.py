

# alpha_list = list('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ')
# with open('american-english.txt') as f :
#     str_content = f.read()
#     values = [str_content.count(v) for v in alpha_list]
#     dict_alpha_count = {k:v for (k,v) in zip(alpha_list,values)}
#     # print(dict_alpha_count)


import string

letters = dict()

# # initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0

# print(letters)

with open('american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)

sort = sorted(letters.items(), key = lambda x : x[1] , reverse = True)
most_freq = sort[0:4]
print(most_freq)
alphabet = dict()
with open('phonetic_alphabet.csv') as f:
    content = f.read().splitlines()
 
for item in content[1:]:
    letters , words = item.split(',')
    alphabet[letters] = words

list = list()
str = input('Enter a String :').upper()
print(str,end='==>> ')

for char in str:
    list.append(alphabet[char])

str = ' '.join(list)

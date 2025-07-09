


with open('american-english.txt') as f :
    content = f.read().splitlines()
    dictionary = {k:v for (k,v) in zip([words for words in content],[len(words) for words in content])}
    print(dictionary)
    

# word_list = sorted(dictionary.items(), key = lambda x : x[1] , reverse = True)
# print(word_list[:100])


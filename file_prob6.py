

def wc(file_name):
    with open(file_name,'r') as f :
        content = f.read().splitlines()
        no_lines  = len(content)
        words = [line.split() for line in content]
        no_words = sum([len(i) for i in words])
        no_char = 0
        for line in content:
            no_char += len(list(line))
        print(f'No. of Lines : {no_lines}\nNo. of Words : {no_words}\nNo. of Characters : {no_char}')

file_name = input('Enter File name : ')
wc(file_name)        


    
# def wc(file):
#     with open(file, 'r') as f:
#         # reading the file into a list
#         content = f.read().splitlines()

#         lines = len(content)

#         words = 0
#         for line in content:
#             words += len(line.split())

#         chars = 0
#         for line in content:
#             chars += len(list(line))

#         return lines, words, chars

# print(wc('sample_file.txt'))
    



    




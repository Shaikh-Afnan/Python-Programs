


with open('test.txt','r') as f:
    content1 = f.read().splitlines()
    

with open('text.txt','r') as f:
    content2 = f.read().splitlines()

file = list(zip(content1,content2)) 
i = 0
for item in file:
    # item = (file1 , file2)
    i += 1
    if item[0] != item[1]:
        print(f'File1 ({i}) : {item[0]} , File2 ({i}) : {item[1]}')
        








with open('test.txt') as f:
    content_list = f.readlines()

tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)   

with open('without_space.txt','w') as f:
    f.write(''.join(tmp_list))
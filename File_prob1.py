

with open('macs.txt') as f:
    contents = f.read().split()
    unique_list = list(set(contents))
    

with open('unique_macs.txt', 'w') as f:
    for ip in unique_list:
        f.write(f'{ip}\n') 




    

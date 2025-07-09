
import time
#                       My solution
def tail(str , lines):
    with open(str) as f:
        contents  = f.read().splitlines()
        start_index = len(contents) - lines
        for i in range(start_index, len(contents)):
            print(contents[i])


file_name = input('Enter file name : ') 
no_lines = int(input('No. of tail line to read : '))
tail(file_name,no_lines)  


#               Infinite loop solution to prob 5
# while True:
#     tail(file_name,no_lines)
#     time.sleep(3)
#     print(' ')


#           Instructor solution
# def tail(file_name,no_lines):
    # with open(file_name) as f:
    #     content = f.read().splitlines()
    #     last_lines = content[len(content) - no_lines:]
    #     str_lines = '\n'.join(last_lines)
    #     print(str_lines) 



with open('test.txt') as f:
    content = f.read().splitlines()
    Deposit , withdrawal =  0 , 0

    list = [line.split(':') for line in content]
    for line in list:
        if line[0] == 'D':
            Deposit += int(line[1])
        elif line[0] == 'W':
            withdrawal += int(line[1])
        else:
            print('File Format Error')
           
    print(Deposit , withdrawal)
    balance = Deposit - withdrawal
    print(balance)


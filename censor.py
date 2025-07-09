
with open("sample.txt") as f:
    sentence = f.read()

sentence = sentence.replace("donkey","######")

with open("sample.txt" ,"w") as f :
    f.write(sentence)




import datetime
firstTime = datetime.datetime.now()
with open("caso01.txt") as file:
    dic = {}
    word = ""
    counter = 1
    for line in file.readlines():
        try:
            word += line.rsplit()[0]
            dic[line.rsplit()[0]] = line.rsplit()[1]
            print("linha " + str(counter))
            counter += 1
        except Exception as e:
            dic[line.rsplit()[0]] = ""
            print("exception " + str(counter))
            counter += 1
        # print(line)
    index = 0
    word2 = word
    while index < len(word2):
        if dic.get(word2[index]) != "":
            word2 = word2.replace(word2[index], dic.get(word2[index]))
        else:
            index += 1
with open("teste1.txt", "w") as file:
    #file.write("tamanho: " + str(len(word2)))
    file.write(word2)
lastTime = datetime.datetime.now()
difference = lastTime - firstTime
# print(dic.items())
# print(word)
# print("")
# print(word2)
print(len(word2))
print(difference.total_seconds())
print("foi")

# 1:     268.297
# 2: 598.497.341

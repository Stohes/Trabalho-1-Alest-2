import datetime
firstTime = datetime.datetime.now()
with open("caso02.txt") as file:
    dic = {}
    word = ""
    for line in file.readlines():
        try:
            word += line.rsplit()[0]
            dic[line.rsplit()[0]] = line.rsplit()[1]
        except Exception as e:
            dic[line.rsplit()[0]] = line.rsplit()[0]

    arr = dic.values()
    for words in arr:
        for char in words:
            word = word.replace(char, "")

    index = 0
# criar dicionario auxiliar com o head e o value do head
    while index < len(word):
        if dic.get(word[index]) != word[index]:
            word = word.replace(word[index], dic.get(word[index]))
        else:
            index += 1

lastTime = datetime.datetime.now()
difference = lastTime - firstTime
print("tamanho: " + str(len(word)))
print("tempo: " + str(difference.total_seconds()))
print("foi")


# fazer letra por letra, por ex A vira mmmooomommmooommooommooommooomommmooommooommooo e nao memimomu FAZER ISSO 1

# fazer um grafico da complexidade da solucao 1


# solucao 1
# 1:     268.297
# 2: 598.497.341

# solucao 2
# 1:     178.833
# 2: 399.461.207

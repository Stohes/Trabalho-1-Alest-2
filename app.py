import datetime
print("comecou")
firstTime = datetime.datetime.now()
with open("caso01.txt") as file:
    dic = {}
    word = ""
    for line in file.readlines():
        try:
            left = line.rsplit()[0]
            right = line.rsplit()[1]
            word += left
            dic[left] = right
        except Exception as e:
            dic[left] = left

dicRights = dic.values()
for right in dicRights:
    for char in right:
        word = word.replace(char, "")
wordSave = word

dic2 = dic.copy()

for key, word in dic2.items():
    index = 0
    while index < len(word):
        left = word[index]
        right = dic2.get(left)

        if left != right:
            word = word.replace(left, right)
        else:
            index += 1
    dic2[key] = word


lastTime = datetime.datetime.now()
difference = lastTime - firstTime
print("tamanho: " + str(len(dic2[wordSave])))
print("tempo: " + str(difference.total_seconds()))
print("foi")


# fazer um grafico da complexidade da solucao 1

# trocar o word para um array

# mudar primeiro todas as letras do dicionario que nao sao a principal

# enquanto tá otimizando o dicionario ir botando as letras finais num auxiliar e removendo do outro e substituir o final no dicionario


# solucao 1
# 1:     268.297
# 2: 598.497.341

# solucao 2
# 1:     178.833    tempo: 0.088989
# 2: 399.461.207    tempo: 202.673274

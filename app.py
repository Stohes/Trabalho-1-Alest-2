import datetime
print("comecou")
firstTime = datetime.datetime.now()
with open("caso06.txt") as file:
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


wordLen = 0
while 0 < len(word):
    left = word[0]
    right = dic.get(left)
    if right != left:
        word = word.replace(left, right)
    else:
        wordLen += word.count(left)
        word = word.replace(left, "")


lastTime = datetime.datetime.now()
difference = lastTime - firstTime
print("wordLen: " + str(wordLen))
print("tempo: " + str(difference.total_seconds()))
print("foi")

# fazer um grafico da complexidade de cada solucao

# solucao 1
# 1:     268.297
# 2:     598.497.341

# solucao 2
# 1:     178.833            tempo: 0.088989
# 2:     399.461.207        tempo: 202.673274
# 3:     15.563.117.040     tempo: 12433.146438

# solucao 3
# 1:     178.833            tempo: 0.005983
# 2:     399.461.207        tempo: 8.168568
# 3:     15.563.117.040     tempo: 257.114382
# 4:     37.554.807.516     tempo: 519.820179
# 5:     26.835.107.381     tempo: 438.110697

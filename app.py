import datetime

print("comecou")
firstTime = datetime.datetime.now()
with open("casos de teste/caso10.txt") as file:
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


dicCharValues = {}


def charValue(char):
    rightValue = 0
    if char in dicCharValues:
        return dicCharValues.get(char)
    else:
        for charac in dic.get(char):
            if charac == dic.get(char):
                return 1
            rightValue += charValue(charac)
            dicCharValues[charac] = charValue(charac)
        return rightValue


wordLen = charValue(word)


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

# solucao 4
# 1:     178.833                    tempo: 0.000988
# 2:     399.461.207                tempo: 0.000953
# 3:     15.563.117.040             tempo: 0.072379
# 4:     37.554.807.516             tempo: 0.009986
# 5:     26.835.107.381             tempo: 0.004985
# 6:     35.172.695.271.276         tempo: 0.005983
# 7:     248.961.376.085            tempo: 0.007012
# 8:     48.024.951.450.717         tempo: 0.010247
# 9:     7.740.687.772.924.768      tempo: 0.008975
# 10:    147.634.677.711            tempo: 0.001985

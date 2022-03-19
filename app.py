
#case = open("caso01.txt", "r")

# print("teste")
# print(case.read())


# def dicCreator(file):  # ler o arquivo e criar o dic

with open("caso01.txt") as file:
    dic = {}
    for line in file.readlines():
        try:
            dic[line.rsplit()[0]] = line.rsplit()[1]
        except Exception as e:
            dic[line.rsplit()[0]] = ""
        print(line)
    print(dic.items())

    # botar readlines[0] na key e [1] no value
    # dicCreator(case)
    # def alg(word, dic):  # passar a palavra de teste e o dic
    #    pass

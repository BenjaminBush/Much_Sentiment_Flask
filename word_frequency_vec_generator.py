import csv
outfile = open(r'/home/kevin/datasets/full_debates_wcvecs.txt', 'w')
performers = ['Hclinton_1', 'Dukakis_1', 'Trump_1', 'Wbush_2', 'Wbush_1', 'Gore_1', 'Carter_2', 'Carter_1', 'Bclinton_2', 'Reagan_1', 'Bclinton_1', 'Obama_1', 'Obama_2', 'Mondale_1', 'Kerry_1', 'Dole_1', 'Mccain_1', 'Reagan_2', 'Romney_1', 'Hwbush_1', 'Kennedy_1', 'Hwbush_2', 'Ford_1', 'Nixon_1', 'Anderson_1']

name_dict_dict = {}
name_dict_dict["overall"] = {}
with open(r'/home/kevin/datasets/full_debates.csv', 'r') as mydeb:
    for line in csv.reader(mydeb):
        if line[0] == "Date":
            continue
        datename = str(line[0])

        demdatename = str(line[0])+str(line[1])
        repdatename = str(line[0])+str(line[2])
        name_dict_dict[datename] = {}
        name_dict_dict[demdatename] = {}
        name_dict_dict[repdatename] = {}


        for word in line[3].split():
            if "(" in word or ")" in word or "[" in word or "]" in word:
                continue
            word = word.replace(";", "")
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.replace("?", "")
            word = word.replace(":", "")
            word = word.replace("!", "")
            word = word.replace("-", "")
            word = ''.join([i for i in word if i.isalpha()])

            word = word.lower()
            if word == "":
                continue

            if word not in name_dict_dict[datename]:
                name_dict_dict[datename][word] = 1
            else:
                name_dict_dict[datename][word] += 1
            if word not in name_dict_dict[demdatename]:
                name_dict_dict[demdatename][word] = 1
            else:
                name_dict_dict[demdatename][word] += 1
            if word not in name_dict_dict["overall"]:
                name_dict_dict["overall"][word] = 1
            else:
                name_dict_dict["overall"][word] += 1
        for word in line[4].split():
            if "(" in word or ")" in word or "[" in word or "]" in word:
                continue
            word = word.replace(";", "")
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.replace("?", "")
            word = word.replace(":", "")
            word = word.replace("!", "")
            word = word.replace("-", "")
            word = ''.join([i for i in word if i.isalpha()])
            word = word.lower()
            if word == "":
                continue

            if word not in name_dict_dict[datename]:
                name_dict_dict[datename][word] = 1
            else:
                name_dict_dict[datename][word] += 1
            if word not in name_dict_dict[repdatename]:
                name_dict_dict[repdatename][word] = 1
            else:
                name_dict_dict[repdatename][word] += 1
            if word not in name_dict_dict["overall"]:
                name_dict_dict["overall"][word] = 1
            else:
                name_dict_dict["overall"][word] += 1
        for word in line[5].split():
            if "(" in word or ")" in word or "[" in word or "]" in word:
                continue
            word = word.replace(";", "")
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.replace("?", "")
            word = word.replace(":", "")
            word = word.replace("!", "")
            word = word.replace("-", "")
            word = ''.join([i for i in word if i.isalpha()])
            word = word.lower()
            if word == "":
                continue

            if word not in name_dict_dict[datename]:
                name_dict_dict[datename][word] = 1
            else:
                name_dict_dict[datename][word] += 1
            if word not in name_dict_dict["overall"]:
                name_dict_dict["overall"][word] = 1
            else:
                name_dict_dict["overall"][word] += 1

mykeys = name_dict_dict.keys()
for x in mykeys:
    if str(x) == 0 or str(x) == 1:
        name_dict_dict.pop(x)
mykeys = sorted(name_dict_dict.keys())
outfile.write("\t".join(["word", "overall"] + mykeys))
for myword in name_dict_dict["overall"].keys():
    myvalues = []
    for k in mykeys:
        myval = name_dict_dict[k].get(myword, 0)
        myvalues.append(myval)

    outfile.write("\t".join([myword, str(name_dict_dict["overall"][myword])] + list([str(trueval) for trueval in myvalues])))
    outfile.write("\n")


outfile.close()


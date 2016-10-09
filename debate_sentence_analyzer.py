import csv

outfile = open(r'/home/kevin/datasets/full_debates_sentencelengths.txt', 'w')
outfile.write("\t".join(["Democrat", "Dem. Sentence Length", "Republican", "Rep. Sentence Length"]))
outfile.write("\n")
with open(r'/home/kevin/datasets/full_debates.csv', 'r') as mydeb:
    for line in csv.reader(mydeb):
        if line[0] == "Date":
            continue
        dem_name = line[1]
        rep_name = line[2]
        dem_para = line[3]
        rep_para = line[4]
        dem_avg = 0
        rep_avg = 0
        dem_sentences = dem_para.split(".")
        for x in dem_sentences:
            y = str(x).split("?")
            if len(y)>1:
                dem_sentences.remove(x)
                for k in y:
                    dem_sentences.append(y)
        rep_sentences = rep_para.split(".")
        for x in rep_sentences:
            y = str(x).split("?")
            if len(y) > 1:
                rep_sentences.remove(x)
                for k in y:
                    rep_sentences.append(y)
        if len(dem_sentences)>2:
            dem_avg = sum([len(x) for x in dem_sentences])/len(dem_sentences)
        if len(rep_sentences) > 2:
            rep_avg = sum([len(x) for x in rep_sentences]) / len(rep_sentences)

        outfile.write("\t".join([dem_name, str(dem_avg), rep_name, str(rep_avg)]))
        outfile.write("\n")
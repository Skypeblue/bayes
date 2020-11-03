import re
import random

def split_lines(input,seed,output1,output2):
    inputFile = open(input,"r")
    outputFile1 = open(output1,"w")
    outputFile2 = open(output2,"w")

    random.seed(seed)

    for line in inputFile:
        if random.random() > 0.5 :
            outputFile1.write(line)
        else :
            outputFile2.write(line)

    inputFile.close()
    outputFile1.close()
    outputFile2.close()

#split_lines("sophie.txt",33,"test.txt","test2.txt")

def tokenize_and_split(sms_file):
    res = {}
    ind = 0
    spam = []
    ham = []
    with open(sms_file,'r') as f:
        for line in f:
            words = line.split() 
            occ = []
            for char in words[1:]:
                if char not in res:
                    res[char] = ind
                    ind += 1
                occ += [res[char]]
            if words[0] == 'ham':
                ham += [occ]                
            else:
                spam += [occ]
    return res,spam,ham

_,_,a=tokenize_and_split("test3_0")

def compute_frequencies(num_words,doc):
    def aux(i,sets):
        count = 0 
        for sub in sets:
            if i in sub:
                count +=1
        return count/len(sets)
    sets = [set(sub) for sub in doc]
    return [aux(i,sets) for i in range(num_words)]

print(compute_frequencies(6,a))

def naive_bayes_train(sms_file):
    words,spam,ham = tokenize_and_split(sms_file)
    spam_ratio = len(spam)/(len(spam)+len(ham))
    spam_freq = compute_frequencies(len(words),spam)
    freq = compute_frequencies(len(words),spam+ham)
    spamcity = [spam_freq[i]/freq[i] for i in range(len(words))]
    return spam_ratio,words,spamcity

print(naive_bayes_train("test3_0"))

def naives_bayes_predict(spam_ratio,words,spamcity,sms):
    
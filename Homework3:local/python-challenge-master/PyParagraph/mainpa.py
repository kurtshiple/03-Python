
f = open('pgone.txt','r')
firstparagraphlist = [line.split(' ') for line in f]
#print(firstparagraphlist)
wordcount = 0
wordlengthlist =[]
for word in firstparagraphlist[0]:
    wordcount = wordcount + 1
    wordlengthlist.append(len(word))
#print(wordcount)
#print(wordlengthlist)
totalwordlength = sum(wordlengthlist)
#print(totalwordlength)
averagewordlength = totalwordlength/wordcount
#print(averagewordlength)




g = open('pgone.txt','r')
firstparagraphlist2 = [line.split('.') for line in g]
#print(firstparagraphlist2)
sentencecount = 0
for sentence in firstparagraphlist2[0]:
    sentencecount = sentencecount + 1
#print(sentencecount)
averagesentencelength = wordcount/sentencecount
#print(averagesentencelength)

print("-------------------------------")
print("Paragraph Analysis: Paragraph 1")
print("-------------------------------")
print(f"Approximate Word Count: {wordcount}")
print(f"Approximate Sentence Count: {sentencecount}")
print(f"Average Letter Count: {averagewordlength}")
print(f"Average Sentence Length: {round(averagesentencelength,2)}")

#-------------------------------------


h = open('pgtwo.txt','r')
rawparagraphlist = [line.split(' ') for line in h]
#print(rawparagraphlist)
secondparagraphlist = []
for sublist in rawparagraphlist:
    for word in sublist:
        secondparagraphlist.append(word)
#print(secondparagraphlist)
newsecondparagraphlist = []
for word in secondparagraphlist:
    if word != "\n":
        newsecondparagraphlist.append(word)
#print(newsecondparagraphlist) 
wordcount2 = 0
wordlengthlist2 =[]
for word in newsecondparagraphlist:
    wordcount2 = wordcount2 + 1
    wordlengthlist2.append(len(word))
#print(wordcount2)
#print(wordlengthlist2)
totalwordlength2 = sum(wordlengthlist2)
#print(totalwordlength2)
averagewordlength2 = totalwordlength2/wordcount2
#print(averagewordlength2)




i = open('pgtwo.txt','r')
rawparagraphlist2 = [line.split('.') for line in i]
#print(rawparagraphlist2)
newsecondparagraphlist2 = []
for sublist in rawparagraphlist2:
    if sublist[0] != "\n":
        newsecondparagraphlist2.append(sublist)
sentencecount2 = 0
#print(newsecondparagraphlist2)
for sentence in newsecondparagraphlist2:
    sentencecount2 = sentencecount2 + 1
#print(sentencecount2)
averagesentencelength2 = wordcount2/sentencecount2
#print(averagesentencelength2)


print("-------------------------------")
print("Paragraph Analysis: Paragraph 2")
print("-------------------------------")
print(f"Approximate Word Count: {wordcount2}")
print(f"Approximate Sentence Count: {sentencecount2}")
print(f"Average Letter Count: {round(averagewordlength2,2)}")
print(f"Average Sentence Length: {round(averagesentencelength2,2)}")

with open('mainpa.txt','w') as f:
        f.write("-------------------------------")
        f.write("Paragraph Analysis: Paragraph 1")
        f.write("-------------------------------")
        f.write(f"Approximate Word Count: {wordcount}")
        f.write(f"Approximate Sentence Count: {sentencecount}")
        f.write(f"Average Letter Count: {averagewordlength}")
        f.write(f"Average Sentence Length: {round(averagesentencelength,2)}")
        f.write("-------------------------------")
        f.write("-------------------------------")
        f.write("Paragraph Analysis: Paragraph 2")
        f.write("-------------------------------")
        f.write(f"Approximate Word Count: {wordcount2}")
        f.write(f"Approximate Sentence Count: {sentencecount2}")
        f.write(f"Average Letter Count: {round(averagewordlength2,2)}")
        f.write(f"Average Sentence Length: {round(averagesentencelength2,2)}")


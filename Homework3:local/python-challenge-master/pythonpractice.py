h = open('pgtwo.txt','r')
secondparagraphlist = [line.split(' ') for line in h]
#print(list(secondparagraphlist))
wordcount2 = 0
wordlengthlist2 =[]
for word in firstparagraphlist[0]:
    wordcount2 = wordcount2 + 1
    wordlengthlist2.append(len(word))
#print(wordcount2)
#print(wordlengthlist2)
totalwordlength2 = sum(wordlengthlist2)
#print(totalwordlength2)
averagewordlength2 = totalwordlength2/wordcount2
#print(averagewordlength2)




i = open('pgtwo.txt','r')
secondparagraphlist2 = [line.split('.') for line in i]
#print(firstparagraphlist2)
sentencecount2 = 0
for sentence in firstparagraphlist2[0]:
    sentencecount2 = sentencecount2 + 1
#print(sentencecount2)
averagesentencelength2 = wordcount2/sentencecount2
#print(averagesentencelength2)

print("Paragraph Analysis: Paragraph 2")
print("-------------------------------")
print(f"Approximate Word Count: {wordcount2}")
print(f"Approximate Sentence Count: {sentencecount2}")
print(f"Average Letter Count: {averagewordlength2}")
print(f"Average Sentence Length: {round(averagesentencelength2,2)}")



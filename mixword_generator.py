words=['apple','orange','lemon','lime','banana'];
from random import randint;#random module in randint function
def randomSentenceGenerator(word):
    randomIndex=randint(0,len(words)-1);
    return f'{words[randomIndex]}{word}'

with open('./text.txt') as file:
    paragraph=file.read();
    wordLists=paragraph.split();
    sentenceList=list(map(randomSentenceGenerator,wordLists))
    para_count=int(input("How many paragraph: "));# change integer
    
    for count in range(para_count):
        with open('./generator.txt','a') as write_file:
            write_file.write(''.join(sentenceList)+'\n\n');
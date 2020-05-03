import numpy as np

f1=open("Sentiment_1.txt")
lines=f1.readlines()
vocabulary_words = []
vectors=[]
vocabulary = { x:i  for x,i in enumerate(vocabulary_words)}
for line in lines :
    line = line[:-1]
    line = line.split(' ')
    vocabulary_words.append(line[0])
    print(line[1:])
    vectors.append(line[1:len(line)-1])

vocabulary = { x:i  for x,i in enumerate(vocabulary_words)}

embeddings = 1 * np.random.randn(len(vocabulary_words) + 1,100)
embeddings[0] = 0 

for index,word in vocabulary.items():
    print(index)
    print(len(vectors[index]))
    embeddings[index] = vectors[index]

print(embeddings)
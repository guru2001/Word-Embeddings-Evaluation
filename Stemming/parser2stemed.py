corpus1=open('sample1PO.txt', "r") #pos_tag_output from this stemming output should be generated
fd1=open("Stemmedoutput1.txt", "w+") #linewise output after stemming 

A = [line.rstrip('\n') for line in corpus1]

for x in range(0,len(A)):
    y=A[x]
    y=y.split('\t')
    if len(y)>1 :
            fd1.write(y[1])
            fd1.write(" ")
    elif len(y)==1 and y[0]=='</s>':
            fd1.write("\n")
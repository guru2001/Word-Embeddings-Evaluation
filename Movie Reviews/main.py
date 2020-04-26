
import re
f1=open("pos_review","r")
text=f1.readlines()

f2=open("reviews.txt","w")
for line in text :
    if line[0]=='_' :
        f2.write('\n')
        # f2.write("  ,1"+'\n')
    else :
        line=re.sub(r'\t',' ',line)
        line=re.sub(r'\n',' ',line)
        line=re.sub(r',','',line)
        # line= re.sub(r'  +','',line)
        # print(line(len(line)-1))
        f2.write(' '.join(line.split()))

f1.close()
# f2.close()

f1=open("neg_review","r")
text=f1.readlines()

# f2=open("neg_labelled.csv","w")
for line in text :
    if line[0]=='_' :
        f2.write('\n')
        # f2.write("  ,-1"+'\n')
    else :
        line=re.sub(r'\t',' ',line)
        line=re.sub(r'\n',' ',line)
        line=re.sub(r',','',line)
        # line= re.sub(r'  +','',line)
        # print(line(len(line)-1))
        f2.write(' '.join(line.split()))


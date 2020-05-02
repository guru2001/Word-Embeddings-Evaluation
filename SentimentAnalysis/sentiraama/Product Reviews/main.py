
import re
f1=open("product_pos.txt","r")
text=f1.readlines()

f2=open("reviews_product.txt","w")
f3=open("pos_labelled.csv","w")
for line in text :
    if line[0]=='_' :
        f2.write( "."+'\n')
        f3.write("  , 1 "+ '.' +'\n')
    else :
        line=re.sub(r'\t',' ',line)
        line=re.sub(r'\n',' ',line)
        line=re.sub(r',','',line)
        # line= re.sub(r'  +','',line)
        # print(line(len(line)-1))
        f2.write(' '.join(line.split()))
        f3.write(' '.join(line.split()))

f1.close()
f3.close()

f1=open("product_neg.txt","r")
text=f1.readlines()

f3=open("neg_labelled.csv","w")
for line in text :
    if line[0]=='_' :
        f2.write("."+'\n')
        f3.write("  , 0 "+ '.' +'\n')
    else :
        line=re.sub(r'\t',' ',line)
        line=re.sub(r'\n',' ',line)
        line=re.sub(r',','',line)
        # line= re.sub(r'  +','',line)
        # print(line(len(line)-1))
        f2.write(' '.join(line.split()))
        f3.write(' '.join(line.split()))


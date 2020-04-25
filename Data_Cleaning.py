import re
f = open("Stemmedoutput1.txt","r")
data = f.read()
# print(data)
# Lines=data.split('.')
# print(Lines)
# print("Done")
# print(len(Lines))
#( Inferiority Complex ) to remove these tyor of characters
data = re.sub(r'\([^)]*\)', '', data)
#alpha numeric characters
data = re.sub('[a-zA-Z]+','',data) 
#
data = re.sub('●','',data)
#Replacing '.' with a new line character
data = re.sub(r'\n+', '\n', data)
#replacing number of white spaces with single white space
data=re.sub(' +',' ',data)
#correcting name with initials 

# for line in Lines: 
#     print(line)

f1 = open("temp.txt", "w") 
f1.write(data)

f2=open("temp.txt","r")
f3=open("Stem&cleaned1.txt","w")
data=f2.read()
Lines=data.split('\n')
i=0
for line in Lines :
    # print(i)
    i=i+1
    # line= re.sub(r'\.','',line)
    # line= re.sub(r'\|','',line)
    # line= re.sub(r'\*','',line)
    # line= re.sub(r'\[','',line)
    # line= re.sub(r'\]','',line)
    # line= re.sub(r'\\','',line)
    # line= re.sub(r'\/','',line)
    # line= re.sub(r'\-','',line)
    # line= re.sub(r'\#','',line)
    #removing unnecessary characters
    line= re.sub(r'  +','',line)
    line= re.sub(r'[\.\|\*\[\]\\\/\-\#\)\(\&\;]','',line)

    # print(line.split())
    if (len(line.split())>0) :
        x=line.split()
        y=str(x[len(x)-1])
        if len(re.sub(r'[^\w\s]','', y))==1 :
            line=line + '.'
            f3.write(line)
        else :
            f3.write(line+'\n')




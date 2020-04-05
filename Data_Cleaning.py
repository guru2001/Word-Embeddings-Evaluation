import re
f = open("sample1.txt","r")
data = f.read()
f.close()
data = re.sub(r'\([^)]*\)', '', data)
data = re.sub('^[a-zA-Z0-9]+$','',data)
data = re.sub('●','',data)

f = open("samplecleaned.txt", "w") 
f.write(data)

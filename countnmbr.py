fr=open("Demo.txt","r")
countlines=0
for line in fr.readlines():
    countlines=countlines+1
print("Number of lines:",countlines)
fr.close()

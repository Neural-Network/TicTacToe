f = open("data.txt")
f2 = open("data2.txt","w")
for line in f:
    newstring = ""
    for i in range(0,9):
        if(int(line[:-1][-1])==i):
            newstring=newstring+"1"
        else:
            newstring=newstring+"0"
    output = line[:-2] + newstring
    f2.write(output+"\n")
    print output
f2.close()

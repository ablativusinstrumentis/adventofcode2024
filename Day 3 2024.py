import re
# first time doing regex lets gooo
s = open("input2.txt","r").read()

m = 'mul\([0-9]*\,[0-9]*\)'
#t = re.compile(m).findall(s)
t = re.compile(m).findall(re.sub(re.compile("don't\(\)(.|\n)*?do\(\)"),'',s)) # its so bad i love it
adddd = 0
for i in range(len(t)):
    list1 = t[i].split(sep=",")
    a = int(list1[0].split(sep="(")[-1])
    b = int(list1[1].split(sep=")")[0])
    
    adddd += (a*b)

print(adddd)


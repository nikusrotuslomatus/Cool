f=open('me.txt','+')
f.write("qunnquu 1")
f.close()
f=open('me.txt','+')

for i in f:
    i=i.split()
    i[1]="2"
f.close()
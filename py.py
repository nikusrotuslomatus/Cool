f=open('me.txt','a+')
f.write('vvvttv 1')
f.close()
f=open('me.txt','r+')
for i in f:
    i=i.split()
    i[1]="2"
f.close()
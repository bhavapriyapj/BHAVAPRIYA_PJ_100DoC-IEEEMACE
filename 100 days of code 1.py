l=list('abcdefghijklmnopqrstuvwxyz')
line=input('Enter the string')
string=''
for a in line:
    g=a.lower()
    if g in l:
        m=str(l.index(g)+1)
        string=string+m+''
    else:
        continue
print(str(string))

        
        

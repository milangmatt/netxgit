digits = input()
key={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
ls=list(key[digits[0]])
for i in range(1,len(digits)):
    h=0
    for j in range(0,len(key[digits[i]])):
        for k in range(1,len(key[digits[i]])):
            ls.insert(h+1,ls[h])
            h+=1
        h+=1*i
    h=0
    for j in range(0,len(key[digits[i]])):
        for k in range(0,len(key[digits[i]])):
            ls[h]=ls[h]+key[digits[i]][k]
            h+=1

print(ls)
def vowel(var):
    newVar=var.lower()
    for i in newVar:
        if i=='a' or i=='e' or i=='u' or i=='o' or i=='i':
            continue
        else:
            print(i)
vowel("Allaa")
#//////////////////////////////////////////////////////
def vowel2(*var):
    vList=["a","e","i","u","o"]
    nlist=[]
    for i in var:
        for j in i.lower():
            if j not in vList:
                nlist.append(j)
    print(nlist)
vowel2("Alaa","lossh","skkhuiop")
#/////////////////////////////////////////////
def vowel3(*newVar):
    var=str(newVar)
    vList = ["a", "e", "i", "u", "o"]
    print(var)
    for word in var:
        if word in vList:
            var=var.replace(word,"")
    print("vowel3")
    print(var)

vowel3(["Alaa","oso","ssi"])
#///////////////////////////////////////////////
def strIndex(strs,char):
    indexList=[]
    i=-1
    for j in strs:
        i += 1
        if char in j:
            indexList.append(strs.index(char,i))
    return indexList
print(strIndex("iihihhiii","i"))
#//////////////////////////////////////////////////////
def num(num1):
    numb=num1+1
    full=[]
    for k in range(1,numb):
        result = []
        for j in range(1,k+1):
            result.append(k*j)
        full.append(result)
    print(full)

num(4)
#/////////////////////////////////////////////////////////
def area(op,*args):
    result=1

    if op=="t" and len(list(args))==2:
        for i in args:
            result *=i;
        print("rect")
        print(result)
    elif op=="r" and len(list(args))==2:
        for i in args:
            result *=i
        result=result*.5
        print("tir")
        print(result)
    elif op=="r" and len(list(args))==1 :
        for i in args:
            result =i*i

        print(result)
    elif op == "c" and len(list(args)) == 1:
        for i in args:
            result = i * i
        result=3.14*result
        print("circle")
        print(result)
    else:
        print("you entered wrong values")


area("r",2)
#///////////////////////////////////////////////////////////
def sp(ListOfStr):
    dec={}
    list=[]
    li = []

    for i in ListOfStr:

        s=i[0][:1]

        if s  not in dec.keys():
            list.append(i)
            dec[s]=list
        elif s in list:
            li.append(i)
            dec[s] = li
    sorted_=sorted(dec.items())
    print(sorted_)

sp(["alaa","ahmed","mahdy"])
#////////////////////////////////////////////////////////////////
def astr(ast):
    astric="*"
    if type(ast)==type(1):
        for i in range(ast+1):
            print(astric*i)
    else:
        print("please enter another int value")
astr(5)
#//////////////////////////////////
## Nicholas Candra
## JC Data Science JKT 07
## Ujian Modul 1 20/12/2019

## Hashtag
def Hashtag(string):
    if len(string) > 140:
        return print(False)
    elif len(string) == 0:
        return print(False)
    else:
        lis = ['#']
        string = string.split()
        for i in string:
            lis.append(i.capitalize())
        return print(''.join(lis))
# Hashtag(" Hello there how are you doing")
# Hashtag("  Hello  World  ")
# Hashtag("")



## Phone Number
def create_phone_number(number):
    if type(number) == list:
        if len(number) < 11 and len(number) > 0:
            l = []
            for i in number:
                l.append(str(i))
            lip = []
            for i in range(3):
                lip.append(l[i])
            li2 = []
            for i in range(3,6):
                li2.append(l[i])
            li3 = []
            for i in range(6,len(l)):
                li3.append(l[i])
            z = ''
            z += '('
            z += ''.join(lip)
            z += ')'
            z += " "
            z += ''.join(li2)
            z += '-'
            z += ''.join(li3)
            return print('"'+z+'"')
        else:
            return print('invalid')
    else:
        return print('input must be list')
# create_phone_number([1,2,3,4,5,6,8,9,0])

##sort odd even
def sort_odd_even(num):
    genap = []
    idxgenap = []
    ganjil = []
    idxganjil = []
    for i in num:
        if i % 2 == 0:
            genap.append(i)
            n = num.index(i)
            idxgenap.append(n)
        elif i % 2 != 0:
            ganjil.append(i)
            o = num.index(i)
            idxganjil.append(o)
    ganjil.sort()
    genap.sort()
    genap = genap[::-1]
    hasil = genap + ganjil
    for j, k in zip(ganjil,idxganjil):
        hasil[k] = j
    for l, m in zip(genap, idxgenap):
        hasil[m] = l
    return print(hasil)
# sort_odd_even([5,3,2,8,1,4])
# sort_odd_even([])



## hollow triangle
def hollowTriangle(height):
    num = 1
    idx = []
    for i in range(height):
        idx.append(num)
        num += 2
    z= ''
    for i in range(height-1):
        for j in range(idx[-1]):
            if j != height-i-1 and j != height+i-1:
                z += '_'
            else: 
                z += '#'
        z += '\n'
    z += '#' * idx[-1]
    return print(z)
# hollowTriangle(6)
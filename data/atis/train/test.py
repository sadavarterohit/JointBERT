a = open('seq.out')
b = open('seq.in')

al = a.readlines()
bl = b.readlines()


for i in range(len(al)):
    if (not len(al[i].split())==len(bl[i].split())):
        print(i,len(al[i].split()),len(bl[i].split()))
        print(al[i].split())
        print(bl[i].split())


a.close()
b.close()

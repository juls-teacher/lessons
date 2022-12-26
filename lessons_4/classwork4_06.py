"""Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m), а также количество x этих чисел."""

n= int(input("vvedi nachalnoe chislo"))
m= int(input ("vvedi poslednee chislo "))
k=0
for i in range(n,m+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print (i)
            k+=1
print("kolichestvo prostih chisel v zadanom diapazone ", k)

"""Используя условие первой задачи из урока, проверить то же самое только для коней."""

x1,y1 = int(input()),int(input())
x2,y2 = int(input()),int (input())

if __name__ =="__main__":


    if (x1-x2==1 or x1-x2==-1) and (y1-y2==-2 or y1-y2==2) :
        print("YES")
    elif (x1-x2==2 or x1-x2==-2) and (y1-y2==-1 or y1-y2==1):
        print("YES")
    else:
        print("NO")

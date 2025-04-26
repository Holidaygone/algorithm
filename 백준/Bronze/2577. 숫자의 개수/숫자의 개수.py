A = int(input())
B = int(input())
C = int(input())

ABC = A * B * C

Num_List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

ABC = str(ABC)

for i in ABC:
    Num_List[int(i)] += 1

for j in Num_List:
    print(j)
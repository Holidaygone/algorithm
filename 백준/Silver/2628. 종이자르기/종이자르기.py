x, y = map(int, input().split())

paper_width = [0, y]
paper_length = [0, x]

N = int(input())

for n in range(N):

    way, line = map(int, input().split())

    if way == 0:
        paper_width.append(line)
    if way == 1:
        paper_length.append(line)

paper_width.sort()
paper_length.sort()
max_area = 0
for b in range(len(paper_length)-1):
    for a in range(len(paper_width)-1):
        temp_area = (paper_width[a+1] - paper_width[a]) * (paper_length[b+1]-paper_length[b])
        if temp_area > max_area:
            max_area = temp_area
# print(paper_width)
# print(paper_length)
print(max_area)
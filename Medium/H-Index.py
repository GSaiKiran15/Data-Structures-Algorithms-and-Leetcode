citations = [3,0,6,1,5]
h = 0
paper_counts = [0]*(len(citations) + 1)

for i in range(len(citations)):
    if citations[i] > len(citations):
        paper_counts[-1] += 1
    else:
        paper_counts[citations[i]] += 1
sum = 0
for i in range(len(paper_counts)-1, -1, -1):
    sum += paper_counts[i]
    if sum >= i:
        print(i)
        break
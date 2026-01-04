citations = [1,3,1]
n = len(citations)
paper_counts = [0] * (len(citations) + 1)

for i in citations:
    paper_counts[min(n, i)] += 1
print(paper_counts)

h = n
papers = paper_counts[n]

while papers < h:
    h -= 1
    papers += paper_counts[h]

print(h)
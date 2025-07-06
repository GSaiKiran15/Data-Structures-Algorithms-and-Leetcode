citations = [3,0,6,1,5]

n = len(citations)

paper_counts = [0] * (n+1)

for c in citations:
    paper_counts[min(n,c)] += 1

h = n

papers = paper_counts[n]

while papers < h:
    h -= 1
    papers += paper_counts[h]

print(h)



# l = [0] * (len(citations)+1)
# for i in citations:
#     if i > len(l)-1:
#         l[-1] += 1
#     else:
#         l[i] += 1
# output = 0
# for i in range(len(l)-1, -1, -1):
#     output += l[i]
#     if i >= output:
#         print(l[i], output)
# else:
#     print(0)
    
    
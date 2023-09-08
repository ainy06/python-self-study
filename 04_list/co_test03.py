P = int(input())
result = ""

for i in range(P):
    data_set = input().split()
    N = int(data_set[0])
    R = data_set[1]
    for j in range(len(R)):
        result += R[j] * N

    result += "\n"

print(result)
